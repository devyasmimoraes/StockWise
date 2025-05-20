from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Cliente, Produto, Venda
from .forms import ProdutoForm, VendaForm
from django.utils.dateparse import parse_date
from .forms import ClienteForm
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm
from django.db.models.functions import TruncDate
from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
@login_required
def dashboard(request):
    total_produtos = Produto.objects.count()
    total_vendas = Venda.objects.count()
    produtos_baixo_estoque = Produto.objects.filter(estoque__lt=5)

    vendas_por_dia = (
        Venda.objects
        .annotate(data_venda=TruncDate('data'))
        .values('data_venda')
        .annotate(total=Sum('quantidade'))
        .order_by('data_venda')
    )

    labels = [v['data_venda'].strftime('%d/%m') for v in vendas_por_dia]
    data = [v['total'] for v in vendas_por_dia]

    return render(request, 'core/dashboard.html', {
        'total_produtos': total_produtos,
        'total_vendas': total_vendas,
        'produtos_baixo_estoque': produtos_baixo_estoque,
        'grafico_labels': labels,
        'grafico_dados': data,
    })
# Produtos
@login_required
def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'core/lista_produtos.html', {'produtos': produtos})
@login_required
def novo_produto(request):
    form = ProdutoForm(request.POST or None, request.FILES or None)  # ✅ Adicionado request.FILES
    if form.is_valid():
        form.save()
        messages.success(request, 'Produto cadastrado com sucesso!')
        return redirect('lista_produtos')
    return render(request, 'core/form_produto.html', {'form': form})

@login_required
def editar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    form = ProdutoForm(request.POST or None, request.FILES or None, instance=produto)  # ✅ Aqui também
    if form.is_valid():
        form.save()
        messages.success(request, 'Produto atualizado!')
        return redirect('lista_produtos')
    return render(request, 'core/form_produto.html', {'form': form})

@login_required
def excluir_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    produto.delete()
    messages.success(request, 'Produto excluído!')
    return redirect('lista_produtos')
@user_passes_test(lambda u: u.is_staff)
def confirmar_exclusao_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        messages.success(request, 'Produto excluído com sucesso!')
        return redirect('lista_produtos')
    return render(request, 'core/confirmar_exclusao_produto.html', {'produto': produto})
# Vendas
@login_required
def lista_vendas(request):
    vendas = Venda.objects.all().order_by('-data')
    data_inicio = request.GET.get('inicio')
    data_fim = request.GET.get('fim')

    if data_inicio:
        vendas = vendas.filter(data__date__gte=parse_date(data_inicio))
    if data_fim:
        vendas = vendas.filter(data__date__lte=parse_date(data_fim))

    return render(request, 'core/lista_vendas.html', {
        'vendas': vendas,
        'data_inicio': data_inicio,
        'data_fim': data_fim
    })
@user_passes_test(lambda u: u.is_staff)
def confirmar_exclusao_venda(request, pk):
    venda = get_object_or_404(Venda, pk=pk)
    if request.method == 'POST':
        venda.delete()
        messages.success(request, 'Venda excluída com sucesso!')
        return redirect('lista_vendas')
    return render(request, 'core/confirmar_exclusao_venda.html', {'venda': venda})

@login_required
def nova_venda(request):
    form = VendaForm(request.POST or None)
    if form.is_valid():
        try:
            venda = form.save(commit=False)
            venda.usuario = request.user  # ✅ quem vendeu
            venda.save()
            messages.success(request, 'Venda realizada com sucesso!')
            return redirect('lista_vendas')
        except ValueError as e:
            messages.error(request, str(e))
    return render(request, 'core/form_venda.html', {'form': form})

@login_required
def lista_clientes(request):
    clientes = Cliente.objects.all().order_by('nome')
    return render(request, 'core/lista_clientes.html', {'clientes': clientes})

@login_required
def novo_cliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Cliente cadastrado com sucesso!')
        return redirect('lista_clientes')
    return render(request, 'core/form_cliente.html', {'form': form})

@login_required
def historico_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    vendas = Venda.objects.filter(cliente=cliente).order_by('-data')
    return render(request, 'core/historico_cliente.html', {
        'cliente': cliente,
        'vendas': vendas
    })

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário criado com sucesso! Faça login.')
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'core/registro.html', {'form': form})

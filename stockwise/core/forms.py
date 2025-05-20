from django import forms
from .models import Produto, Venda
from .models import Cliente
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'estoque', 'imagem']  # ✅ inclua imagem

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['produto', 'cliente', 'quantidade', 'observacao']  # ✅ adicionar cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone', 'cpf_cnpj']  # incluído aqui


class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
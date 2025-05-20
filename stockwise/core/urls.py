from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    # Produtos
    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('produtos/novo/', views.novo_produto, name='novo_produto'),
    path('produtos/editar/<int:pk>/', views.editar_produto, name='editar_produto'),
    path('produtos/excluir/<int:pk>/', views.excluir_produto, name='excluir_produto'),

    # Vendas
    path('vendas/', views.lista_vendas, name='lista_vendas'),
    path('vendas/nova/', views.nova_venda, name='nova_venda'),

    # Clientes
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/novo/', views.novo_cliente, name='novo_cliente'),
    path('clientes/<int:cliente_id>/historico/', views.historico_cliente, name='historico_cliente'),
    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),
    path('registro/', views.registrar_usuario, name='registro'),
    path('vendas/<int:pk>/confirmar-exclusao/', views.confirmar_exclusao_venda, name='confirmar_exclusao_venda'),
    path('produtos/<int:pk>/confirmar-exclusao/', views.confirmar_exclusao_produto, name='confirmar_exclusao_produto'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

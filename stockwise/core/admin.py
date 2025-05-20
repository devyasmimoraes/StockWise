from django.contrib import admin
from .models import Produto, Venda, Cliente

admin.site.register(Produto)
admin.site.register(Cliente)

class VendaAdmin(admin.ModelAdmin):
    list_display = ('produto', 'quantidade', 'cliente', 'usuario', 'data')

admin.site.register(Venda, VendaAdmin)

from django.contrib import admin

from .models import Loja
class LojaAdmin(admin.ModelAdmin):
    fields = ('categoria', 'nome', 'slug', 'imagem', 'descricao', 'data_cadastro')
    list_display = ['nome', 'slug', 'categoria','imagem', 'descricao', 'data_cadastro']
    search_fields = ['nome', 'imagem', 'descricao']
    list_filter = ['categoria']
    list_editable = ['categoria', 'imagem', 'descricao']
    prepopulated_fields = {'slug': ('nome',)}


admin.site.register(Loja, LojaAdmin)
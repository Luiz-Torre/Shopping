from django.contrib import admin

from teatro.models import Teatro


class TeatroAdmin(admin.ModelAdmin):
    fields = ('nome', 'slug', 'imagem', 'descricao')
    list_display = ['nome', 'slug','imagem', 'descricao']
    search_fields = ['nome', 'imagem', 'descricao']
    list_filter = ['nome']
    list_editable = ['imagem', 'descricao']
    prepopulated_fields = {'slug': ('nome',)}

admin.site.register(Teatro,TeatroAdmin)

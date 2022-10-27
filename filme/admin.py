from django.contrib import admin


from filme.models import Filme


class FilmeAdmin(admin.ModelAdmin):
    fields = ('genero', 'nome', 'slug', 'imagem', 'descricao', 'data_lancamento')
    list_display = ['nome', 'slug', 'genero','imagem', 'descricao', 'data_lancamento']
    search_fields = ['nome', 'imagem', 'descricao']
    list_filter = ['genero']
    list_editable = ['genero', 'imagem', 'descricao']
    prepopulated_fields = {'slug': ('nome',)}

admin.site.register(Filme,FilmeAdmin)

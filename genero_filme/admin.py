from django.contrib import admin

from genero_filme.models import GeneroFilme


class GeneroFilmeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug']
    search_fields = ['nome', 'slug']
    prepopulated_fields = {'slug': ('nome',)}

admin.site.register(GeneroFilme,GeneroFilmeAdmin)

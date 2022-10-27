from django.core.paginator import Paginator
from django.shortcuts import render

from filme.models import Filme


def filmes(request):
        lista_filmes = Filme.objects.all().order_by('nome')
        paginator = Paginator(lista_filmes,3)
        pagina = request.GET.get('pagina')
        page_obj = paginator.get_page(pagina)
        return render(request, 'filme/filmes.html', {'filmes': page_obj})

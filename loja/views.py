from django.core.paginator import Paginator
from django.shortcuts import render

from loja.forms import PesquisaLojaForm
from loja.models import Loja


def lista_loja(request):
    form = PesquisaLojaForm(request.GET)
    if form.is_valid():
        nome = form.cleaned_data['nome']
        lista_de_lojas = Loja.objects.filter(nome__icontains=nome).order_by('nome')
        paginator = Paginator(lista_de_lojas,3)
        pagina = request.GET.get('pagina')
        page_obj = paginator.get_page(pagina)
        return render(request, 'loja/pesquisa_loja.html', {'lojas': page_obj,
                                                           'form':form,
                                                            'nome':nome})

    else:
        raise ValueError("Ocorreu um erro inesperado ao tentar recuperar a loja")

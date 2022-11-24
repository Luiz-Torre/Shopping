from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render
from django.template.defaultfilters import slugify

from loja.forms import PesquisaLojaForm, LojaForm
from loja.models import Loja


def lista_loja(request):
    form = PesquisaLojaForm(request.GET)
    if form.is_valid():
        nome = form.cleaned_data['nome']
        lista_de_lojas = Loja.objects.filter(nome__icontains=nome).order_by('nome')
        paginator = Paginator(lista_de_lojas, 3)
        pagina = request.GET.get('pagina')
        page_obj = paginator.get_page(pagina)
        return render(request, 'loja/pesquisa_loja.html', {'lojas': page_obj,
                                                           'form': form,
                                                           'nome': nome})

    else:
        raise ValueError("Ocorreu um erro inesperado ao tentar recuperar a loja")


def cadastra_loja(request):

    if request.POST:
        loja_form = LojaForm(request.POST)

        if loja_form.is_valid():
            loja = loja_form.save(commit=False)
            loja.slug = slugify(loja.nome)
            loja.save()
            messages.add_message(request, messages.INFO, 'Loja cadastrada com sucesso')
            return render(request, 'loja/exibe_loja.html', {'loja': loja})
    else:
        loja_form = LojaForm()


    return render(request, 'loja/cadastra_loja.html', {'form': loja_form})

from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
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
        loja_id = request.session.get('loja_id')
        if loja_id:
            loja = get_object_or_404(Loja, pk= loja_id)
            loja_form = LojaForm(request.POST, request.FILES, instance=loja)

        else:
            loja_form = LojaForm(request.POST, request.FILES)

        if loja_form.is_valid():
            loja = loja_form.save(commit=False)
            loja.slug = slugify(loja.nome)
            loja.save()

            if loja_id:
                messages.add_message(request, messages.INFO, 'Loja alterada com sucesso')
                del request.session['loja_id']
            else:
                messages.add_message(request, messages.INFO, 'Loja cadastrada com sucesso')

            return redirect('loja:exibe_loja', id = loja.id)

    else:
        try:
            del request.session['loja_id']
        except KeyError:
            pass
        loja_form = LojaForm()


    return render(request, 'loja/cadastra_loja.html', {'form': loja_form})
def exibe_loja(request, id):
    loja = get_object_or_404(Loja, pk = id)
    request.session['loja_id_del'] = id
    return render(request, 'loja/exibe_loja.html', {'loja': loja})


def edita_loja(request, id):
    loja = get_object_or_404(Loja, pk=id)
    loja_form = LojaForm(instance=loja)
    request.session['loja_id'] = id
    return render(request, 'loja/cadastra_loja.html', {'form': loja_form})


def remove_loja(request):
    loja_id = request.session.get('loja_id_del')
    loja = get_object_or_404(Loja, id=loja_id)
    loja.imagem.delete()
    loja.delete()
    del request.session['loja_id_del']
    messages.add_message(request, messages.INFO, 'Loja removido com sucesso.')
    return render(request, 'loja/exibe_loja.html', {'loja': loja})

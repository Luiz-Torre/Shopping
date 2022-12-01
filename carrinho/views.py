import locale
from decimal import Decimal

from django.contrib import messages
from django.core import serializers
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.signing import Signer
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.defaultfilters import slugify
from carrinho.carrinho import Carrinho_Function
from carrinho.forms import CarrinhoForm, QuantidadeForm
from carrinho.models import Carrinho
from categoria.models import Categoria


def lista_produtos(request, slug_da_categoria=None):
    lista_de_produtos = Carrinho.objects.all().order_by('nome')
    if slug_da_categoria:
        categoria = get_object_or_404(Categoria, slug=slug_da_categoria)
        lista_de_produtos = lista_de_produtos.filter(categoria=categoria).order_by('nome')

    paginator = Paginator(lista_de_produtos, 12)
    pagina = request.GET.get('pagina')
    try:
        produtos = paginator.page(pagina)
    except PageNotAnInteger:
        produtos = paginator.page(1)
    except EmptyPage:
        if request.is_ajax():
            return HttpResponse('')
        produtos = paginator.page(paginator.num_pages)

    carrinho = Carrinho_Function(request)
    carrinho_form = CarrinhoForm()

    lista_de_forms = []
    for produto in produtos:
        qtd = produto.quantidade
        lista_de_forms.append(QuantidadeForm(initial={'quantidade': qtd, 'produto_id': produto.id}))

    preco_total = carrinho.get_preco_carrinho()
    if request.is_ajax():
        return render(request, 'carrinho/pagina_de_produtos.html', {'listas': zip(produtos, lista_de_forms), 'preco_total': preco_total, 'form': carrinho_form})

    carrinho_form = CarrinhoForm()
    return render(request, 'carrinho/lista_produtos.html', {'listas': zip(produtos, lista_de_forms), 'preco_total': preco_total, 'form': carrinho_form})



def cadastra_produto(request):

    if request.POST:
        carrinho_form = CarrinhoForm(request.POST)

        if carrinho_form.is_valid():
            carrinho = carrinho_form.save()
            carrinho2 = Carrinho_Function(request)
            carrinho2.atualiza(carrinho.id, carrinho.quantidade)
            messages.add_message(request, messages.INFO, 'Produto cadastrado com sucesso')
            carrinho.categoria = carrinho.categoria

            ser_instance = serializers.serialize('json', [ carrinho, ])

            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            return JsonResponse({"error": carrinho_form.errors}, status=400)
    else:
        JsonResponse({"error": ""}, status=400)


def atualiza_carrinho(request):
    form = QuantidadeForm(request.POST)
    print(request.POST)
    if form.is_valid():
        produto_id = form.cleaned_data['produto_id']
        quantidade = form.cleaned_data['quantidade']
        produto = get_object_or_404(Carrinho, pk=produto_id)
        produto.quantidade = quantidade
        carrinho2 = Carrinho_Function(request)
        if quantidade == 0:
            produto.delete()
            carrinho2.remover(produto_id)
            messages.add_message(request, messages.INFO, 'Loja removido com sucesso.')
        else:
            carrinho2.atualiza(produto_id, quantidade)
            produto.save()
            request.session['carrinho_id'] = produto_id

        preco_total = carrinho2.get_preco_carrinho()


        return JsonResponse({'quantidade': quantidade, 'preco_total': preco_total })
    else:
        raise ValueError('Ocorreu um erro inesperado ao adicionar um produto ao carrinho.')



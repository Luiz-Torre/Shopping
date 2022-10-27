from django.shortcuts import render

from loja.models import Loja


def index(request):
    lista_de_lojas = Loja.objects.filter()[:6]
    print(lista_de_lojas)
    return render(request, 'index.html', {'lojas': lista_de_lojas})


def sobre(request):
    return render(request, 'sobre.html')


def contato(request):
    return render(request, 'contato.html')


def lazer(request):
    return render(request, 'lazer.html')

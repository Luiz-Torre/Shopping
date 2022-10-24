from django.shortcuts import render


def index(request):
    frase = "Esta frase está sendo exebida pelo indext da loja"
    return render(request, 'loja/index.html', {'texto_loja':frase})
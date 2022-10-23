from django.shortcuts import render


def index(request):
        frase = "Frase do index"
        return render(request, 'index.html', {'texto': frase})
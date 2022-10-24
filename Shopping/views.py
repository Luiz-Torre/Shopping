from django.shortcuts import render


def index(request):
        frase = "Frase do index"
        return render(request, 'index.html', {'texto': frase})

def sobre(request):
        frase = "Frase do sobre"
        return render(request, 'sobre.html', {'texto': frase})
def contato(request):
        frase = "Frase do contato"
        return render(request, 'sobre.html', {'texto': frase})
def lazer(request):
        frase = "Frase do lazer"
        return render(request, 'sobre.html', {'texto': frase})
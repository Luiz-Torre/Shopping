from django.shortcuts import render

from teatro.models import Teatro


def teatro(request):
    lista_pecas = Teatro.objects.all().order_by('nome')
    return render(request, 'teatro/pecas_teatro.html', {'pecas': lista_pecas})

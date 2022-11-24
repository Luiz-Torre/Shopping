from django.shortcuts import render



# Create your views here.
def pedido(request):

    return render(request, 'pedido/pedidos.html')
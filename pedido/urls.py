from django.urls import path

from pedido import views

app_name = 'pedido'

urlpatterns = [
    path('pedidos/', views.pedido, name='pedido')

]
from django.urls import path

from loja import views

app_name = 'loja'

urlpatterns = [
    path('lista_loja/', views.lista_loja, name='lista_loja')
]
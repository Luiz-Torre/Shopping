from django.urls import path

from carrinho import views

app_name = 'carrinho'

urlpatterns =[
   path('lista_produtos/', views.lista_produtos, name='lista_produtos'),
   path('cadastra_produto/', views.cadastra_produto, name='cadastra_produto'),
   path('atualiza_carrinho/', views.atualiza_carrinho, name='atualiza_carrinho'),
]
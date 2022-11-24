from django.urls import path

from loja import views

app_name = 'loja'

urlpatterns = [
    path('lista_loja/', views.lista_loja, name='lista_loja'),
    path('cadastra_loja/', views.cadastra_loja, name='cadastra_loja'),
    path('exibe_loja/<int:id>', views.exibe_loja, name='exibe_loja'),
    path('edita_loja/<int:id>', views.edita_loja, name='edita_loja'),
    path('remove_loja/', views.remove_loja, name='remove_loja')

]
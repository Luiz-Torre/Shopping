from django.urls import path

from filme import views

app_name = 'filmes'

urlpatterns = [
    path('filmes/', views.filmes, name='filmes')

]
from django.urls import path

from teatro import views

app_name = 'teatro'

urlpatterns = [
    path('pecas/', views.teatro, name='teatro')

]
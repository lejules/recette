from django.urls import path
from . import views

app_name = 'recette'

urlpatterns = [
    path('', views.index, name='index'),
    path('ajout_recette', views.ajout_recette, name='ajout_recette'),
]
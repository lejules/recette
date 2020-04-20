from django.urls import path
from . import views

app_name = 'recette'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:recette_id>/', views.detail, name='detail'),
    path('ajout_recette', views.ajout_recette, name='ajout_recette'),
    path('<int:recette_id>/ajout_ingredient', views.ajout_ingredient, name='ajout_ingredient'),
]
from django.urls import path
from . import views

app_name = 'recette'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:recette_id>/', views.detail, name='detail'),
    path('ajout_recette', views.ajout_recette, name='ajout_recette'),
    path('<int:recette_id>/ajout_ingredient', views.ajout_ingredient, name='ajout_ingredient'),
    path('<int:ingredient_id>/supprimer_ingredient/', views.supprimer_ingredient, name='supprimer_ingredient'),
    path('<int:commentaire_id>/supprimer_commentaire/', views.supprimer_commentaire, name='supprimer_commentaire'),
    path('<int:recette_id>/modifier_recette', views.modifier_recette, name='modifier_recette'),
    path('<int:recette_id>/ajout_commentaire', views.ajout_commentaire, name='ajout_commentaire'),
]
from django import forms
from .models import Recette, Media, Ingredient


class formRecette(forms.ModelForm):

    class Meta:
        model = Recette
        exclude = ['nombre_visite', 'utilisateur']


class formMedia(forms.ModelForm):

    class Meta:
        model = Media
        exclude = ['recette']


class formIngredient(forms.ModelForm):

    class Meta:
        model = Ingredient
        exclude = ['recette']
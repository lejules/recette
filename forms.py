from django import forms
from .models import Recette


class formRecette(forms.ModelForm):

    class Meta:
        model = Recette
        exclude = ['nombre_visite', 'utilisateur']
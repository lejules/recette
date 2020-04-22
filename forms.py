from django import forms
from .models import Recette, Media, Ingredient, Commentaire
from django.utils.translation import gettext_lazy as _


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


class formCommentaire(forms.ModelForm):

    class Meta:
        model = Commentaire
        fields = ('description', )
        labels = {'description': _('Votre commentaire :')}
        help_texts = {'description': _('Pensez à enregistrer votre commentaire !')}
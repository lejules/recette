from django.db import models
from django.contrib.auth.models import User
from django.core.validators import URLValidator

# Create your models here.
class Recette(models.Model):

    class NiveauDeDifficulte(models.TextChoices):
        FACILE = 'F', _('Facile')
        MOYEN = 'M', _('Moyen')
        DIFFICILE = 'D', _('Difficile')

    class NiveauDeCout(models.TextChoices):
        FAIBLE = 'F', _('Faible')
        MOYEN = 'M', _('Moyen')
        ELEVE = 'E', _('Eleve')

    titre = models.CharField(max_length=255)
    description = models.TextField()
    nombre_visite = models.IntegerField()
    nombre_mangeur = models.IntegerField(max_length=3)
    difficulte = models.CharField(max_length=1,
                                  choices=NiveauDeDifficulte.choices,
                                  default=NiveauDeDifficulte.FACILE)
    cout = models.CharField(max_length=1,
                            choices=NiveauDeCout.choices,
                            default=NiveauDeCout.MOYEN)
    calorie = models.IntegerField(max_length=5)
    temps_preparation = models.IntegerField(max_length=4)
    temps_cuisson = models.IntegerField(max_length=4)
    temps_repos = models.IntegerField(max_length=4)
    ustensile = models.CharField(max_length=255)
    cree = models.DateTimeField(auto_now_add=True)
    maj = models.DateTimeField(auto_now=True)
    cuisson = models.ForeignKey(Cuisson, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    particularite = models.ForeignKey(Particularite, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(User)


class Cuisson(models.Model):
    nom = models.CharField(max_length=30)


class Type(models.Model):
    nom = models.CharField(max_length=30)


class Particularite(models.Model):
    nom = models.CharField(max_length=30)


class Ingredient(models.Model):
    designation = models.CharField(max_length=255)
    quantite = models.DecimalField(max_digits=7, decimal_places=1)
    ordre = models.IntegerField(max_length=2)
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE)


class Media(models.Model):
    photo = models.ImageField()
    url = models.CharField(max_length=255, validators=[URLValidator])
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE)


class Commentaire(models.Model):
    description = models.TextField()
    cree = models.DateTimeField(auto_now_add=True)
    maj = models.DateTimeField(auto_now=True)
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE)
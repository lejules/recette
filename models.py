from django.db import models
from datetime import date
from django.contrib.auth.models import User


# Create your models here.
class Recette(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    nombre_visite = models.IntegerField()
    nombre_mangeur = models.IntegerField(max_length=3)
    difficulte = models.IntegerField(max_length=1)
    cout = models.IntegerField(max_length=1)
    calorie = models.IntegerField(max_length=5)
    temps_preparation = models.IntegerField(max_length=4)
    temps_cuisson = models.IntegerField(max_length=4)
    temps_repos = models.IntegerField(max_length=4)
    ustensile = models.CharField(max_length=255)
    cree = models.DateTimeField(auto_now_add=True)
    maj = models.DateTimeField(auto_now=True)


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
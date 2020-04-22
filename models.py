from django.db import models
from django.contrib.auth.models import User
from django.core.validators import URLValidator
from django.utils.translation import gettext_lazy as _


# Create your models here.
def recette_directory_path(instance, filename):
    # MEDIA_ROOT/recette_<id>/<filename>
    return 'recette/_{0}/{1}'.format(instance.recette.id, filename)


class Cuisson(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom


class Type(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom


class Particularite(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom


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
    nombre_visite = models.IntegerField(default=0)
    nombre_mangeur = models.IntegerField(default=0)
    difficulte = models.CharField(max_length=1,
                                  choices=NiveauDeDifficulte.choices,
                                  default=NiveauDeDifficulte.FACILE)
    cout = models.CharField(max_length=1,
                            choices=NiveauDeCout.choices,
                            default=NiveauDeCout.MOYEN)
    calorie = models.IntegerField(default=0)
    temps_preparation = models.IntegerField()
    temps_cuisson = models.IntegerField(default=0)
    temps_repos = models.IntegerField(default=0)
    ustensile = models.CharField(max_length=255)
    cree = models.DateTimeField(auto_now_add=True)
    maj = models.DateTimeField(auto_now=True)
    cuisson = models.ForeignKey(Cuisson, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    particularite = models.ForeignKey(Particularite, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.titre


class Ingredient(models.Model):
    designation = models.CharField(max_length=255)
    quantite = models.DecimalField(max_digits=7, decimal_places=1)
    ordre = models.IntegerField(default=0)
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE)

    def __str__(self):
        return self.designation


class Media(models.Model):
    photo = models.ImageField(upload_to=recette_directory_path)
    url = models.CharField(max_length=255, validators=[URLValidator])
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE)

    def __str__(self):
        return self.url


class Commentaire(models.Model):
    description = models.TextField()
    cree = models.DateTimeField(auto_now_add=True)
    maj = models.DateTimeField(auto_now=True)
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.cree)

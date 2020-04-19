from django.contrib import admin
from .models import Recette, Cuisson, Commentaire, Particularite, Type, Media

# Register your models here.
class RecetteAdmin(admin.ModelAdmin):
    list_display = ('titre', 'temps_preparation', 'nombre_mangeur', 'cree')


class CuissonAdmin(admin.ModelAdmin):
    list_display = ('nom', )


class TypeAdmin(admin.ModelAdmin):
    list_display = ('nom', )


class ParticulariteAdmin(admin.ModelAdmin):
    list_display = ('nom', )


class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('description', 'cree')


class MediaAdmin(admin.ModelAdmin):
    # list_display = ('photo', 'url', 'recette_id')
    fieldsets = [('Recette', {'fields': ['recette']}), ('Les médias', {'fields': ['photo', 'url']}), ]
    view_on_site = False


admin.site.register(Recette, RecetteAdmin)
admin.site.register(Cuisson, CuissonAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Particularite, ParticulariteAdmin)
admin.site.register(Commentaire, CommentaireAdmin)
admin.site.register(Media, MediaAdmin)
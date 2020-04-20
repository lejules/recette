from django.contrib.auth.decorators import login_required
from .models import Recette, Media
from django.forms import formset_factory
from  django.urls import reverse
from django.shortcuts import render, HttpResponseRedirect
from .forms import formRecette, formMedia


# Create your views here.
def index(request):
    recettes = Recette.objects.all()[:6]
    mot = 'Très bien, aucune erreur à afficher'
    return render(request, 'recette/index.html', {'recettes': recettes, 'mot':mot})

@login_required
def ajout_recette(request) :
    # On associe 2 formulaires dans un seul avec un préfixe
    # pour éviter les confusions de champs
    # RecetteFormSet = formset_factory(formRecette)
    # MediaFormSet = formset_factory(formMedia)
    if request.method == 'POST':
        #form = formRecette(request.POST)
        recette_formset = formRecette(request.POST, prefix='recette')
        media_formset = formMedia(request.POST, request.FILES, prefix='media')
        if recette_formset.is_valid() and media_formset.is_valid():
            recette = recette_formset.save(commit=False)
            recette.utilisateur_id = request.user.id
            recette.save()
            media = media_formset.save(commit=False)
            media.recette_id = recette.id
            media.save()
            return HttpResponseRedirect(reverse('recette:index'))
        else:
            recettes = Recette.objects.all()[:6]
            mot = 'Erreur : '+str(media_formset.is_valid())
            return render(request, 'recette/index.html', {'recettes': recettes, 'mot': mot})

    else:
        #form = formRecette()
        # recette_formset = RecetteFormSet(prefix='recette')
        # media_formset = MediaFormSet(prefix='media')
        #return render(request, 'recette/ajout_recette.html', {'form':form})
        recette_formset = formRecette(prefix='recette')
        media_formset = formMedia(prefix='media')
    return render(request, 'recette/ajout_recette.html',
                      {'recette_formset': recette_formset, 'media_formset':media_formset})


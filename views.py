from django.contrib.auth.decorators import login_required
from .models import Recette, Media, Commentaire
from django.forms import formset_factory
from  django.urls import reverse
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .forms import formRecette, formMedia, formIngredient


# Create your views here.
def index(request):
    recettes = Recette.objects.all()[:6]
    mot = 'Très bien, aucune erreur à afficher'
    return render(request, 'recette/index.html', {'recettes': recettes, 'mot':mot})


def detail(request, recette_id):
    recette = get_object_or_404(Recette, pk=recette_id)
    return render(request, 'recette/detail.html', {'recette':recette,})


@login_required(login_url='../admin/login?next=/recette/')
def ajout_recette(request) :
    # On associe 2 formulaires dans un seul avec un préfixe
    # pour éviter les confusions de champs
    if request.method == 'POST':
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
        recette_formset = formRecette(prefix='recette')
        media_formset = formMedia(prefix='media')
    return render(request, 'recette/ajout_recette.html',
                      {'recette_formset': recette_formset, 'media_formset':media_formset})


@login_required(login_url='../admin/login?next=/recette/')
def ajout_ingredient(request, recette_id):
    IngredientFormSet = formset_factory(formIngredient, extra=8)
    if request.method == 'POST':
        listeIngredients = IngredientFormSet(request.POST)
        if listeIngredients.is_valid():
            for form in listeIngredients:
                if form.has_changed():
                    test = form.save(commit=False)
                    test.recette_id = recette_id
                    form.save()
        else:
            print(str(listeIngredients.errors))
        recette = get_object_or_404(Recette, pk=recette_id)
        return render(request, 'recette/index.html',
                      {'recette': recette, 'liste_formulaire_ingredient': IngredientFormSet})
    else:
        recette = get_object_or_404(Recette, pk=recette_id)
        return render(request, 'recette/ajout_ingredient.html',
                  {'recette': recette, 'liste_formulaire_ingredient': IngredientFormSet})
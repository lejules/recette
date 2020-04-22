from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Recette, Ingredient, Media, Commentaire
from django.forms import formset_factory
from django.urls import reverse
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, HttpResponse
from .forms import formRecette, formMedia, formIngredient, formCommentaire


# Create your views here.
def index(request):
    if request.method == 'POST':
        recherche = request.POST["s"]
        recettes = Recette.objects.filter(titre__icontains=recherche)
    else:
        recettes = Recette.objects.order_by("?")
    pagination = Paginator(recettes, 9)
    numero_page = request.GET.get('page')
    page_obj = pagination.get_page(numero_page)
    aff_footer = Recette.objects.order_by("-cree")[:4]
    return render(request, 'recette/index.html', {'page_obj': page_obj, 'aff_footer': aff_footer, })


def detail(request, recette_id):
    recette = get_object_or_404(Recette, pk=recette_id)
    commentaire_form = formCommentaire()
    return render(request, 'recette/detail.html', {'recette':recette, 'commentaire_form': commentaire_form, })


@login_required(login_url='../admin/login?next=/recette/')
def ajout_commentaire(request, recette_id):
    if request.method == 'POST':
        testForm = formCommentaire(request.POST)
        if testForm.is_valid():
            formComm = testForm.save(commit=False)
            formComm.recette_id = recette_id
            formComm.utilisateur_id = request.user.id
            formComm.save()
    return HttpResponseRedirect(reverse('recette:detail', args=(recette_id,)))


@login_required(login_url='../admin/login?next=/recette/')
def supprimer_commentaire(request, commentaire_id):
    if request.method == 'GET':
        test_commentaire = get_object_or_404(Commentaire, pk=commentaire_id)
        if test_commentaire.utilisateur_id == request.user.id:
            test_commentaire.delete()
    return HttpResponse('Commentaire supprimé !')


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
            return HttpResponseRedirect(reverse('recette:ajout_ingredient', args=(recette.id,)))
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
    recette = get_object_or_404(Recette, pk=recette_id)
    # On gère les données déjà inscrites dans les ingrédients de cette recette
    listeIngredients = recette.ingredient_set.all()
    listeIngre = list()
    for ing in listeIngredients:
        dic = {'id': ing.id,
               'designation': ing.designation,
               'quantite': ing.quantite,
               'ordre': ing.ordre,}
        listeIngre.append(dic)
    formset = formset_factory(formIngredient, extra=8)
    IngredientFormSet = formset(initial=listeIngre)
    # Si on enregistre, on teste le tout avec ces données initiales pour ne pas enregistrer 2 fois
    if request.method == 'POST':
        listeIngredients = formset(request.POST, initial=listeIngre)
        if listeIngredients.is_valid():
            for form in listeIngredients:
                if form.has_changed():
                    test = form.save(commit=False)
                    test.recette_id = recette_id
                    form.save()
        else:
            print(str(listeIngredients.errors))

        return HttpResponseRedirect(reverse('recette:detail', args=(recette_id,)))
    else:
        recette = get_object_or_404(Recette, pk=recette_id)
        return render(request, 'recette/ajout_ingredient.html',
                  {'recette': recette, 'liste_formulaire_ingredient': IngredientFormSet})


@login_required(login_url='../admin/login?next=/recette/')
def supprimer_ingredient(request, ingredient_id) :
    ingredient = Ingredient.objects.get(pk=ingredient_id)
    ingredient.delete()
    return HttpResponse('Ingrédient supprimé !')


@login_required(login_url='../admin/login?next=/recette/')
def modifier_recette(request, recette_id) :
    recette = get_object_or_404(Recette, pk=recette_id)
    # # On gère les données déjà inscrites dans les ingrédients de cette recette
    dicRecette = {'id': recette.id, 'titre': recette.titre,
                   'description': recette.description,
                   'nombre_mangeur': recette.nombre_mangeur, 'difficulte': recette.difficulte,
                   'cout': recette.cout, 'calorie': recette.calorie, 'temps_preparation': recette.temps_preparation,
                   'temps_cuisson': recette.temps_cuisson, 'temps_repos': recette.temps_repos,
                   'ustensile': recette.ustensile, 'cuisson': recette.cuisson,
                   'particularite': recette.particularite, 'type': recette.type, }

    if request.method == 'POST':
        recette_formset = formRecette(request.POST, instance=recette, initial=dicRecette)
        # media_formset = formMedia(request.POST, request.FILES, prefix='media', initial=dicMedia)
        if recette_formset.is_valid():
            # and media_formset.is_valid():
            recetteUpdate = recette_formset.save(commit=False)
            recetteUpdate.utilisateur_id = request.user.id
            recetteUpdate.save()
            # media = media_formset.save(commit=False)
            # media.recette_id = recette.id
            # media_formset.save()
            return HttpResponseRedirect(reverse('recette:detail', args=(recette_id,)))
        else:
            recettes = Recette.objects.all()[:6]
            mot = 'Erreur : '+str(recette_formset.is_valid())
            return render(request, 'recette/index.html', {'recettes': recettes, 'mot': mot, })
    else:
        recette_formset = formRecette(initial=dicRecette)
        # return render(request, 'recette/modifier_recette.html', {'recette_formset': recette_formset, })
        recettes = Recette.objects.all()[:6]
        # mot = 'Erreur : ' + str(recette_formset)
        # return render(request, 'recette/index.html', {'recettes': recettes, 'mot': mot, })
        return render(request, 'recette/modifier_recette.html', {'recette_formset': recette_formset, 'recette': recette, })
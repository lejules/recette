from django.shortcuts import render, HttpResponseRedirect
from .forms import formRecette


# Create your views here.
def index(request):
    info = 'salut les terriens'
    return render(request, 'recette/index.html', {'info': info})


def ajout_recette(request) :
    if request.method == 'POST':
        form = formRecette(request.POST)
        if form.is_valid():
            recette = form.save(commit=False)
            recette.utilisateur_id = request.user.id
            recette.save()
            return HttpResponseRedirect('')
    else:
        form = formRecette()
        return render(request, 'recette/ajout_recette.html', {'form':form})

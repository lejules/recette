from django.shortcuts import render
from .models import Recette, Media


# Create your views here.
def index(request):
    recettes = Recette.objects.all()[:6]
    return render(request, 'recette/index.html', {'recettes': recettes})
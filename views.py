from django.shortcuts import render


# Create your views here.
def index(request):
    info = 'Coucou qui voilou ?'
    return render(request, 'recette/index.html', {'info': info})
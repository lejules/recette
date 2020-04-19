from django.shortcuts import render


# Create your views here.
def index(request):
    info = 'salut les terriens'
    return render(request, 'recette/index.html', {'info': info})
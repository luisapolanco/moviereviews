from django.http import HttpResponse
from django.shortcuts import render

from .models import Movie

def home(request):
    #return HttpResponse('<h1>Welcome to Home Page</h1>')
    searchTerm = request.GET.get('searchMovie')
    # if searchTerm:
    #     movies = Movie.objects.filter(title=searchTerm)
    # else:
    #     movies = Movie.objects.all()
    return render(request, 'home.html', {'searchTerm': searchTerm})

def about(request):
    return render(request, 'about.html')
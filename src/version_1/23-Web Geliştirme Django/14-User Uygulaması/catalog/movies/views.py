from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from .models import Movie

# Create your views here.

def index(request):
    movies = Movie.objects.all()

    context = {
        'movies': movies
    }
    return render(request, 'movies/list.html', context)

def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk = movie_id)
    context = {
        'movie': movie
    }
    return render(request, 'movies/detail.html', context)

def search(request):
    return render(request, 'movies/search.html')


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Movies
# Create your views here.


def index(request):
    movies = Movies.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})
    # # SELECT * from movies_movie
    # Movies.objects.filter(release_year=1985)
    # # SELECT * from movies_movie WHERE release_year=1985
    # Movies.objects.get(id=1)


def detail(request, movie_id):
    # can use pk(pick) instead of id
    #movie = Movies.objects.get(id=movie_id)
    movie = get_object_or_404(Movies, id=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})

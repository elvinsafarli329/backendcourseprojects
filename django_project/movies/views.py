from django.shortcuts import render
from .models import Movies


# Create your views here.
def main_page(request):
    return render(request, 'index.html')

def movies_page(request):
    movies_data = Movies.objects.all()
    return render(request, 'movies.html', {"movies_data": movies_data})

def my_movies_page(request):
    movies_data = Movies.objects.all()
    return render(request, 'mymovies.html', {"movies_data": movies_data})


def about_page(request):
    return render(request, 'about.html')


from django.shortcuts import render, redirect
from .models import Movies
from .forms import AddMovieForm

# Create your views here.
def main_page(request):
    return render(request, 'index.html')

def movies_page(request):
    movies_data = Movies.objects.all()
    return render(request, 'movies.html', {"movies_data": movies_data})

def about_page(request):
    return render(request, 'about.html')

def add_movies_page(request):
    form = AddMovieForm(request.POST or None)
    if form.is_valid():
        moviess = form.save(commit=False)
        moviess.recommender = request.user
        moviess.save()
        return redirect("add-movies")
    context = {"form": form}

    return render(request, "add_movies.html", context)
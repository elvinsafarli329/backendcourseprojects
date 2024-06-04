from django.shortcuts import render, redirect, get_object_or_404
from .models import Movies
from .forms import AddMovieForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from django.http import HttpResponse
# from django.template import loader

# Create your views here.
def main_page(request):
    return render(request, 'index.html')

@login_required(login_url="account:login")
def movies_page(request):
    # movies_data = Movies.objects.all().order_by('name')
    movies_data = Movies.objects.all()
    return render(request, 'movies.html', {"movies_data": movies_data})

def about_page(request):
    return render(request, 'about.html')

@login_required(login_url="account:login")
def add_movies_page(request):
    form = AddMovieForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        moviess = form.save(commit=False)
        moviess.recommender = request.user
        moviess.save()
        return redirect("add-movies")
    context = {"form": form}

    return render(request, "add_movies.html", context)

def detail_page(request, id):
    # movie = Movies.objects.filter(id = id).first()
    movie = get_object_or_404(Movies, id = id)
    context = {"movie": movie}
    return render(request, "detail.html", context)

@login_required(login_url="account:login")
def update_movies_page(request, id):
    moviess = get_object_or_404(Movies, id = id)
    form = AddMovieForm(request.POST or None, request.FILES or None, instance=moviess)
    if form.is_valid():
        # moviess = form.save(commit=False)
        # moviess.recommender = request.user
        moviess.save()
        messages.success(request, "Movie content is updated!!")
        return redirect("movies")
    context = {"form": form}

    return render(request, "update_movies.html", context)


@login_required(login_url="account:login")
def delete_movies_page(request, id):
    movie = get_object_or_404(Movies, id = id)
    movie.delete()
    messages.success(request, "Movie content is deleted!!")
    return redirect("movies")

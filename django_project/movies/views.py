from django.shortcuts import render, redirect, get_object_or_404
from .models import Movies, WriteComment
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

# Create your views here.
def main_page(request):
    return render(request, 'index.html')

@login_required(login_url="account:login")
def movies_page(request):
    # movies_data = Movies.objects.all().order_by('name')
    keyword = request.GET.get("keyword")
    if keyword:
        movies_data = Movies.objects.filter(name__icontains=keyword)
        return render(request, 'movies.html', {"movies_data": movies_data})
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
    comments = WriteComment.objects.filter(movie = movie)
    context = {"movie": movie, "comments": comments}
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

@login_required(login_url="account:login")
def add_comment(request, id):
    movie = get_object_or_404(Movies, id = id)

    if request.method == "POST":
        comment_author = request.POST.get('commenter')
        comment_content = request.POST.get('comment_content')

        newComment = WriteComment(commenter = comment_author, comment_content = comment_content)

        newComment.movie = movie
        newComment.save()
        messages.success(request, "Comment has been added!")

    return redirect(reverse("detail", kwargs={"id":id}))

from django.utils.decorators import method_decorator


@method_decorator(login_required(login_url='account:login'), name='dispatch')
class ChangePasswordView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('main')
    template_name = 'settings.html'
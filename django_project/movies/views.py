from django.shortcuts import render
from .models import Movies


# Create your views here.
def main_page(request):
    movies_data = Movies.objects.all()
    return render(request, 'index.html', {"movies_data": movies_data})
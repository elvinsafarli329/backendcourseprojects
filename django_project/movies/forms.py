from django import forms
from .models import Movies

class AddMovieForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ["name", "year", "category", "detail", "image"]
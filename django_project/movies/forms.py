from django import forms
from .models import Movies

class AddMovieForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ["name", "year", "category", "detail", "image"]

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput())
    new_password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())


# class ChangeProfile(forms.Modelform):
#     class Meta:
#         model = CustomUser
#         fields = ['profile_photo']
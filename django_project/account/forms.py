from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    email = forms.EmailField()
    username = forms.CharField(max_length=30, label="Username")
    password = forms.CharField(max_length=10, label="Password", widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=10, label="Confirm the password", widget=forms.PasswordInput)
    
    def clean(self):
        email = self.cleaned_data["email"]
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]
        confirm = self.cleaned_data["confirm"]
        
        
        if password != confirm:
            raise forms.ValidationError("passwords are not the same")
        if User.objects.filter(username=username):
            raise forms.ValidationError("this user already exists")
        if User.objects.filter(email=email):
            raise forms.ValidationError("someone has registered with this email")
        
        values = {
            "email": email,
            "username": username,
            "password": password
        }
        
        return values
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, label="Username")
    password = forms.CharField(max_length=10, label="Password", widget=forms.PasswordInput)

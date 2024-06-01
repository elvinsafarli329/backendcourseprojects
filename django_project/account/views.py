from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, ContactForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.
def register_page(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        email = form.cleaned_data.get('email')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        
        newUser = User(username = username, email=email)
        newUser.set_password(password)
        
        newUser.save()
    
        login(request, newUser)
        messages.success(request, "you are signed in successfully...")
        
        return redirect("main") 
    context = {
        "form":form,
    }
    return render(request, "register.html", context)

def login_page(request):
    form = LoginForm(request.POST or None)
    
    context = {"form": form,}
    
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is None:
            return render(request, "login.html")
        
        login(request, user)
        messages.success(request, "you are logged in successfully...")
        return redirect("main")
    return render(request, "login.html", context)

def logout_page(request):
    logout(request)
    return redirect("main")

def contact_page(request):
    form = ContactForm(request.POST or None)
    context = {"form": form}

    if form.is_valid():
        form.save()
        messages.success(request, "Your message has been sent successfully.")
        return redirect('success')
    return render(request, 'contact.html', context)

def success_view(request):
    return render(request, 'success.html')

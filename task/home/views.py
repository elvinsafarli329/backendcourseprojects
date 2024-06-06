from django.shortcuts import render, redirect
from .forms import PortfolioForm
from django.contrib import messages
# Portfolio modeli qurulmalı
# * En azi 10 field olmali (CharField & TextField)

# Html sehifesinde formumuzu qurmali ve saytimizdan databazamiza datalarin gonderilmesi:
# * Bootstrap istifade ederek

def resume_create(request):
    form = PortfolioForm(request.POST or None)

    context = {"form": form}

    if form.is_valid():
        form.save()
        messages.success(request, "Your detailes have been added.")
        return redirect("resume")
    return render(request, 'cvms.html', context)

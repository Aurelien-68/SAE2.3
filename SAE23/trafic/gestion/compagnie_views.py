from django.shortcuts import render, redirect
from .models import Compagnie
from .forms import CompagnieForm

def compagnie_affiche(request):
    compagnies = Compagnie.objects.all()
    return render(request, 'compagnie/affiche.html', {'compagnies': compagnies})

def compagnie_ajout(request):
    if request.method == 'POST':
        form = CompagnieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('compagnie_affiche')
    else:
        form = CompagnieForm()
    return render(request, 'compagnie/ajout.html', {'form': form})

def compagnie_update(request, id):
    compagnie = Compagnie.objects.get(id=id)
    if request.method == 'POST':
        form = CompagnieForm(request.POST, instance=compagnie)
        if form.is_valid():
            form.save()
            return redirect('compagnie_affiche')
    else:
        form = CompagnieForm(instance=compagnie)
    return render(request, 'compagnie/update.html', {'form': form})
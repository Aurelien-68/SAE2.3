from django.shortcuts import render, redirect
from .models import Aeroport
from .forms import AeroportForm

def aeroport_affiche(request):
    aeroports = Aeroport.objects.all()
    return render(request, 'aeroport/affiche.html', {'aeroports': aeroports})

def aeroport_ajout(request):
    if request.method == 'POST':
        form = AeroportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('aeroport_affiche')
    else:
        form = AeroportForm()
    return render(request, 'aeroport/ajout.html', {'form': form})

def aeroport_update(request, id):
    aeroport = Aeroport.objects.get(id=id)
    if request.method == 'POST':
        form = AeroportForm(request.POST, instance=aeroport)
        if form.is_valid():
            form.save()
            return redirect('aeroport_affiche')
    else:
        form = AeroportForm(instance=aeroport)
    return render(request, 'aeroport/update.html', {'form': form})
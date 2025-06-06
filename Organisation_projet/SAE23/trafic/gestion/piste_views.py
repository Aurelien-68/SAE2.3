from django.shortcuts import render, redirect
from .models import Piste
from .forms import PisteForm

def piste_affiche(request):
    pistes = Piste.objects.select_related('aeroport').all()
    return render(request, 'piste/affiche.html', {'pistes': pistes})

def piste_ajout(request):
    if request.method == 'POST':
        form = PisteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('piste_affiche')
    else:
        form = PisteForm()
    return render(request, 'piste/ajout.html', {'form': form})

def piste_update(request, id):
    piste = Piste.objects.get(id=id)
    if request.method == 'POST':
        form = PisteForm(request.POST, instance=piste)
        if form.is_valid():
            form.save()
            return redirect('piste_affiche')
    else:
        form = PisteForm(instance=piste)
    return render(request, 'piste/update.html', {'form': form})
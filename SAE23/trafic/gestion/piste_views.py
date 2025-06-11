from django.shortcuts import render, redirect, get_object_or_404
from .models import Piste
from .forms import PisteForm
from django.shortcuts import get_object_or_404

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
    piste = get_object_or_404(Piste, pk=id)
    if request.method == 'POST':
        form = PisteForm(request.POST, instance=piste)
        if form.is_valid():
            form.save()
            return redirect('piste_affiche')
    else:
        form = PisteForm(instance=piste)
    return render(request, 'piste/update.html', {'form': form})

def piste_delete(request, id):
    piste = get_object_or_404(Piste, pk=id)
    if request.method == 'POST':
        piste.delete()
        return redirect('piste_affiche')
    return render(request, 'piste/delete.html', {'piste': piste})


def piste_detail(request, id):
    piste_obj = get_object_or_404(Piste, pk=id)
    return render(request, 'piste/detail.html', {'piste': piste_obj})

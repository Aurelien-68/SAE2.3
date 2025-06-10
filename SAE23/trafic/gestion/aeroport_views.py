from django.shortcuts import render, redirect, get_object_or_404
from .models import Aeroport
from .forms import AeroportForm
from django.shortcuts import get_object_or_404

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
    aeroport = get_object_or_404(Aeroport, pk=id)
    if request.method == 'POST':
        form = AeroportForm(request.POST, instance=aeroport)
        if form.is_valid():
            form.save()
            return redirect('aeroport_affiche')
    else:
        form = AeroportForm(instance=aeroport)
    return render(request, 'aeroport/update.html', {'form': form})

def aeroport_delete(request, id):
    aeroport = get_object_or_404(Aeroport, pk=id)
    if request.method == 'POST':
        aeroport.delete()
        return redirect('aeroport_affiche')
    return render(request, 'aeroport/delete.html', {'aeroport': aeroport})


def aeroport_detail(request, id):
    aeroport_obj = get_object_or_404(Aeroport, pk=id)
    return render(request, 'aeroport/detail.html', {'aeroport': aeroport_obj})

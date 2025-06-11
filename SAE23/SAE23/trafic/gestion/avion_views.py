from django.shortcuts import render, redirect, get_object_or_404
from .models import Avion
from .forms import AvionForm
from django.shortcuts import get_object_or_404

def avion_affiche(request):
    avions = Avion.objects.select_related('compagnie', 'modele').all()
    return render(request, 'avion/affiche.html', {'avions': avions})

def avion_ajout(request):
    if request.method == 'POST':
        form = AvionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('avion_affiche')
    else:
        form = AvionForm()
    return render(request, 'avion/ajout.html', {'form': form})

def avion_update(request, id):
    avion = get_object_or_404(Avion, pk=id)
    if request.method == 'POST':
        form = AvionForm(request.POST, instance=avion)
        if form.is_valid():
            form.save()
            return redirect('avion_affiche')
    else:
        form = AvionForm(instance=avion)
    return render(request, 'avion/update.html', {'form': form})

def avion_delete(request, id):
    avion = get_object_or_404(Avion, pk=id)
    if request.method == 'POST':
        avion.delete()
        return redirect('avion_affiche')
    return render(request, 'avion/delete.html', {'avion': avion})


def avion_detail(request, id):
    avion_obj = get_object_or_404(Avion, pk=id)
    return render(request, 'avion/detail.html', {'avion': avion_obj})

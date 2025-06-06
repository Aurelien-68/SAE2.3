from django.shortcuts import render, redirect
from .models import Avion
from .forms import AvionForm

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
    avion = Avion.objects.get(id=id)
    if request.method == 'POST':
        form = AvionForm(request.POST, instance=avion)
        if form.is_valid():
            form.save()
            return redirect('avion_affiche')
    else:
        form = AvionForm(instance=avion)
    return render(request, 'avion/update.html', {'form': form})
from django.shortcuts import render, redirect
from .models import TypeAvion
from .forms import TypeAvionForm

def typeavion_affiche(request):
    types = TypeAvion.objects.all()
    return render(request, 'typeavion/affiche.html', {'types': types})

def typeavion_ajout(request):
    if request.method == 'POST':
        form = TypeAvionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('typeavion_affiche')
    else:
        form = TypeAvionForm()
    return render(request, 'typeavion/ajout.html', {'form': form})

def typeavion_update(request, id):
    type_avion = TypeAvion.objects.get(id=id)
    if request.method == 'POST':
        form = TypeAvionForm(request.POST, request.FILES, instance=type_avion)
        if form.is_valid():
            form.save()
            return redirect('typeavion_affiche')
    else:
        form = TypeAvionForm(instance=type_avion)
    return render(request, 'typeavion/update.html', {'form': form})
from django.shortcuts import render, redirect, get_object_or_404
from .models import TypeAvion
from .forms import TypeAvionForm
from django.shortcuts import get_object_or_404



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
    type_avion = get_object_or_404(TypeAvion, pk=id)
    if request.method == 'POST':
        form = TypeAvionForm(request.POST, request.FILES, instance=type_avion)
        if form.is_valid():
            form.save()
            return redirect('typeavion_affiche')
    else:
        form = TypeAvionForm(instance=type_avion)
    return render(request, 'typeavion/update.html', {'form': form})

def typeavion_delete(request, id):
    type_avion = get_object_or_404(TypeAvion, pk=id)
    if request.method == 'POST':
        type_avion.delete()
        return redirect('typeavion_affiche')
    return render(request, 'typeavion/delete.html', {'type_avion': type_avion})


def typeavion_detail(request, id):
    typeavion_obj = get_object_or_404(TypeAvion, pk=id)
    return render(request, 'typeavion/detail.html', {'typeavion': typeavion_obj})

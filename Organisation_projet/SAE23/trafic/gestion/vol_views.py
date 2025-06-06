from django.shortcuts import render, redirect, get_object_or_404
from .models import Vol
from .forms import VolForm

def vol_affiche(request):
    vol = Vol.objects.all()
    return render(request, 'vol/affiche.html', {'vol': vol})

def vol_ajout(request):
    if request.method == 'POST':
        form = VolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vol_affiche')
    else:
        form = VolForm()
    return render(request, 'vol/ajout.html', {'form': form})

def vol_update(request, id):
    vol = get_object_or_404(Vol, pk=id)
    if request.method == 'POST':
        form = VolForm(request.POST, instance=vol)
        if form.is_valid():
            form.save()
            return redirect('vol_affiche')
    else:
        form = VolForm(instance=vol)
    return render(request, 'vol/update.html', {'form': form})

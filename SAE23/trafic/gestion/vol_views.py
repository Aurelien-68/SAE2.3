from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from datetime import timedelta
from .models import Vol, Piste, Avion, Aeroport
from .forms import VolForm, VolImportForm
import csv, io

def vol_affiche(request):
    vols = Vol.objects.select_related('avion', 'aeroport_depart', 'aeroport_arrivee').all()
    return render(request, 'vol/affiche.html', {'vols': vols})

 
def vol_ajout(request):
    message = ""
    if request.method == 'POST':
        form = VolForm(request.POST)
        if form.is_valid():
            vol = form.save(commit=False)
            type_avion = vol.avion.modele
            aeroport = vol.aeroport_arrivee
            longueur_necessaire = type_avion.longueur_piste_necessaire

            pistes_compatibles = Piste.objects.filter(
                aeroport=aeroport,
                longueur__gte=longueur_necessaire
            )

            piste_disponible = None
            for piste in pistes_compatibles:
                conflits = Vol.objects.filter(
                    aeroport_arrivee=aeroport,
                    date_heure_arrivee__range=[
                        vol.date_heure_arrivee - timedelta(minutes=10),
                        vol.date_heure_arrivee + timedelta(minutes=10)
                    ]
                )
                if not conflits.exists():
                    piste_disponible = piste
                    break

            if piste_disponible:
                vol.save()
                return redirect('vol_affiche')
            else:
                message = "Aucune piste compatible n'est disponible à cette heure."
    else:
        form = VolForm()
    return render(request, 'vol/ajout.html', {'form': form, 'message': message})

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

def vol_delete(request, id):
    vol = get_object_or_404(Vol, pk=id)
    if request.method == 'POST':
        vol.delete()
        return redirect('vol_affiche')
    return render(request, 'vol/delete.html', {'vol': vol})

def vol_import(request):
    message = ""
    success_count = 0
    error_lines = []
    if request.method == "POST":
        form = VolImportForm(request.POST, request.FILES)
        if form.is_valid():
            aeroport = form.cleaned_data['aeroport']
            fichier = form.cleaned_data['fichier']
            decoded_file = fichier.read().decode('utf-8')
            io_string = io.StringIO(decoded_file)
            reader = csv.reader(io_string, delimiter=',')

            # Ignorer la première ligne si c'est l'en-tête
            first_row = next(reader)
            if first_row != ['avion_id', 'pilote', 'date_heure_depart', 'aeroport_arrivee_id', 'date_heure_arrivee']:
                # Si ce n'est pas l'en-tête, on la traite
                io_string.seek(0)
                reader = csv.reader(io_string, delimiter=',')

            for i, row in enumerate(reader, start=1):
                if len(row) != 5:
                    error_lines.append(f"Ligne {i} : nombre de colonnes incorrect")
                    continue
                try:
                    avion_id = int(row[0])
                    pilote = row[1]
                    date_heure_depart = row[2]
                    aeroport_arrivee_id = int(row[3])
                    date_heure_arrivee = row[4]

                    # Vérifier que les objets existent
                    avion = Avion.objects.get(pk=avion_id)
                    aeroport_arrivee = Aeroport.objects.get(pk=aeroport_arrivee_id)

                    Vol.objects.create(
                        avion=avion,
                        pilote=pilote,
                        aeroport_depart=aeroport,
                        date_heure_depart=date_heure_depart,
                        aeroport_arrivee=aeroport_arrivee,
                        date_heure_arrivee=date_heure_arrivee
                    )
                    success_count += 1
                except Avion.DoesNotExist:
                    error_lines.append(f"Ligne {i} : Avion ID {avion_id} inconnu")
                except Aeroport.DoesNotExist:
                    error_lines.append(f"Ligne {i} : Aéroport arrivée ID {aeroport_arrivee_id} inconnu")
                except Exception as e:
                    error_lines.append(f"Ligne {i} : Erreur {str(e)}")

            message = f"Import terminé : {success_count} lignes ajoutées.<br>"
            if error_lines:
                message += "Erreurs :<br>" + "<br>".join(error_lines)
        else:
            message = "Formulaire invalide."
    else:
        form = VolImportForm()

    return render(request, 'vol/import.html', {'form': form, 'message': message})
def vol_detail(request, id):
    vol = get_object_or_404(Vol, pk=id)
    return render(request, 'vol/detail.html', {'vol': vol})

def vol_fiche(request):
    vols = []
    aeroport_id = request.GET.get('aeroport')
    date = request.GET.get('date')
    direction = request.GET.get('direction')
    aeroports = Aeroport.objects.all()

    if aeroport_id and date and direction:
        if direction == 'depart':
            vols = Vol.objects.filter(aeroport_depart_id=aeroport_id, date_heure_depart__date=date)
        elif direction == 'arrivee':
            vols = Vol.objects.filter(aeroport_arrivee_id=aeroport_id, date_heure_arrivee__date=date)

    return render(request, 'vol/fiche.html', {'vols': vols, 'aeroports': aeroports})

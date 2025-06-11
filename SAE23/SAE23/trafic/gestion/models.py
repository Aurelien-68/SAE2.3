from django.db import models

class Aeroport(models.Model):
    nom = models.CharField(max_length=100)
    pays = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nom} ({self.pays})"

class Piste(models.Model):
    numero = models.CharField(max_length=10)
    aeroport = models.ForeignKey(Aeroport, on_delete=models.CASCADE)
    longueur = models.IntegerField(help_text="Longueur en mètres")

    def __str__(self):
        return f"Piste {self.numero} - {self.aeroport.nom}"

class Compagnie(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    pays_rattachement = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class TypeAvion(models.Model):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='type_avions/', blank=True)
    longueur_piste_necessaire = models.IntegerField(help_text="Longueur minimale requise en mètres")

    def __str__(self):
        return f"{self.marque} {self.modele}"

class Avion(models.Model):
    nom = models.CharField(max_length=100)
    compagnie = models.ForeignKey(Compagnie, on_delete=models.CASCADE)
    modele = models.ForeignKey(TypeAvion, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom} ({self.compagnie.nom})"

class Vol(models.Model):
    avion = models.ForeignKey(Avion, on_delete=models.CASCADE)
    pilote = models.CharField(max_length=100)
    aeroport_depart = models.ForeignKey(Aeroport, related_name='departs', on_delete=models.CASCADE)
    date_heure_depart = models.DateTimeField()
    aeroport_arrivee = models.ForeignKey(Aeroport, related_name='arrivees', on_delete=models.CASCADE)
    date_heure_arrivee = models.DateTimeField()

    def __str__(self):
        return f"Vol {self.id}: {self.aeroport_depart} → {self.aeroport_arrivee}"
@property
def duree(self):
    if self.date_heure_depart and self.date_heure_arrivee:
        delta = self.date_heure_arrivee - self.date_heure_depart
        hours, remainder = divmod(delta.seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        return f"{hours}h{minutes:02d}"
    return "N/A"
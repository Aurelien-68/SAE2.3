from django import forms
from .models import *

class AeroportForm(forms.ModelForm):
    class Meta:
        model = Aeroport
        fields = '__all__'

class PisteForm(forms.ModelForm):
    class Meta:
        model = Piste
        fields = '__all__'
        widgets = {
            'longueur': forms.NumberInput(attrs={'class': 'form-control', 'min': '1000'})
        }

class TypeAvionForm(forms.ModelForm):
    class Meta:
        model = TypeAvion
        fields = '__all__'
        widgets = {
            'longueur_piste_necessaire': forms.NumberInput(attrs={'class': 'form-control'})
        }

class CompagnieForm(forms.ModelForm):
    class Meta:
        model = Compagnie
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3})
        }

class AvionForm(forms.ModelForm):
    class Meta:
        model = Avion
        fields = '__all__'
        
class VolForm(forms.ModelForm):
     class Meta:
        model = Avion
        fields = '__all__'
    
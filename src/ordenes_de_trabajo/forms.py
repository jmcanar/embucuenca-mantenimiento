from django import forms
from .models import OrdenTrabajo

class OrdenTrabajoForm(forms.ModelForm):
    class Meta:
        model = OrdenTrabajo
        fields = [
            'codigo', 
            'maquina', 
            'sintoma', 
            'tecnico_asignado', 
            'estado', 
            'inicio_parada',   # Debe coincidir con models.py
            'fin_parada'       # Debe coincidir con models.py
        ]
        widgets = {
            'inicio_parada': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'fin_parada': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
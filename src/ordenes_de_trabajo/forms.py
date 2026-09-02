from django import forms
from .models import OrdenTrabajo

class OrdenTrabajoForm(forms.ModelForm):
    class Meta:
        model = OrdenTrabajo
        fields = ['codigo', 'maquina', 'sintoma', 'tecnico_asignado', 'estado', 'fecha_inicio_parada', 'fecha_fin_parada']
        widgets = {
            'fecha_inicio_parada': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'fecha_fin_parada': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'sintoma': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }
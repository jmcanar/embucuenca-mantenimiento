from django.db import models
from django.core.exceptions import ValidationError

class OrdenTrabajo(models.Model):
    # Campos principales de la Orden de Trabajo
    codigo = models.CharField(max_length=50, verbose_name="Código de Orden")
    maquina = models.CharField(max_length=100, verbose_name="Máquina")
    sintoma = models.TextField(verbose_name="Síntoma o Falla")
    tecnico_asignado = models.CharField(
        max_length=100, 
        blank=True, 
        null=True, 
        verbose_name="Técnico Asignado"
    )
    estado = models.CharField(
        max_length=20, 
        default="PENDIENTE", 
        verbose_name="Estado de la Orden"
    )

    # Campos de registro de tiempos de parada (Requerimiento RF-09 / CP-01)
    inicio_parada = models.DateTimeField(
        blank=True, 
        null=True, 
        verbose_name="Inicio de Parada"
    )
    fin_parada = models.DateTimeField(
        blank=True, 
        null=True, 
        verbose_name="Fin de Parada"
    )

    def clean(self):
        """
        Validación del modelo (CP-01):
        Verifica que la fecha de fin de parada no sea anterior a la de inicio.
        """
        super().clean()
        if self.inicio_parada and self.fin_parada:
            if self.fin_parada < self.inicio_parada:
                raise ValidationError(
                    "La fecha de fin de parada no puede ser anterior a la fecha de inicio."
                )

    def __str__(self):
        """
        Representación en texto del objeto (Requerido para PU-02).
        """
        return f"Orden {self.codigo} - {self.maquina}"
from django.db import models

class OrdenTrabajo(models.Model):
    ESTADO_OPCIONES = [
        ('PENDIENTE', 'Pendiente'),
        ('EN_PROCESO', 'En Proceso'),
        ('FINALIZADO', 'Finalizado'),
    ]
    
    codigo = models.CharField(max_length=20, unique=True)
    maquina = models.CharField(max_length=100) # Relacionado al inventario de máquinas
    sintoma = models.TextField()
    tecnico_asignado = models.CharField(max_length=100, blank=True, null=True) # RF-05[cite: 2]
    estado = models.CharField(max_length=20, choices=ESTADO_OPCIONES, default='PENDIENTE')
    fecha_inicio_parada = models.DateTimeField(blank=True, null=True) # RF-09[cite: 2]
    fecha_fin_parada = models.DateTimeField(blank=True, null=True) # RF-09[cite: 2]
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Orden {self.codigo} - {self.maquina}"
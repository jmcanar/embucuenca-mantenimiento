from django.test import TestCase
from .models import OrdenTrabajo

class OrdenTrabajoModelTest(TestCase):
    
    def setUp(self):
        self.orden = OrdenTrabajo.objects.create(
            codigo="OT-001",
            maquina="Cortadora Principal",
            sintoma="Vibración excesiva en el motor detectada por operario",
            tecnico_asignado="Juan Pérez",
            estado="PENDIENTE"
        )

    def test_creacion_orden(self):
        """PU-02: Comprueba que la orden se crea con estado inicial PENDIENTE"""
        self.assertEqual(self.orden.estado, "PENDIENTE")
        self.assertEqual(str(self.orden), "Orden OT-001 - Cortadora Principal")

    def test_asignacion_tecnico(self):
        """PU-03: Valida que el técnico asignado se almacene correctamente"""
        self.assertEqual(self.orden.tecnico_asignado, "Juan Pérez")
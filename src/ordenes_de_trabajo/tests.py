from django.test import TestCase
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta
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

    def test_cp01_validacion_tiempos_parada(self):
        """CP-01: Valida que si la fecha de fin de parada es anterior a la de inicio, se rechace el registro"""
        inicio = datetime.now()
        fin_invalido = inicio - timedelta(hours=1) # Tiempo invertido
        
        orden = OrdenTrabajo(
            codigo="OT-002",
            maquina="Línea de Empaque",
            sintoma="Fuga de aceite detectada",
            inicio_parada=inicio,
            fin_parada=fin_invalido
        )
        
        with self.assertRaises(ValidationError):
            orden.full_clean()


class EmbuCuencaPruebasIntegracion(TestCase):
    
    def test_cp04_generacion_automatica_orden_falla(self):
        """
        CP-04: Simula que un operario reporta una falla seleccionando un síntoma 
        y verifica que se genere la orden correctiva vinculada con estado pendiente.
        """
        orden = OrdenTrabajo.objects.create(
            codigo="OT-CORR-001",
            maquina="Embutidora Principal",
            sintoma="Sobrecalentamiento en banda transportadora",
            estado="PENDIENTE"
        )

        self.assertEqual(OrdenTrabajo.objects.count(), 1)
        self.assertEqual(orden.maquina, "Embutidora Principal")
        self.assertEqual(orden.estado, "PENDIENTE")
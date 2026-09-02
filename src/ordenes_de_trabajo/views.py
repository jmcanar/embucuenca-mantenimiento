from django.shortcuts import render, redirect
from .models import OrdenTrabajo

def lista_ordenes(view_request):
    ordenes = OrdenTrabajo.objects.all().order_by('-creado_en')
    return render(view_request, 'ordentrabajo/lista.html', {'ordenes': ordenes})
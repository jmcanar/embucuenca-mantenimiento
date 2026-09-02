from django.shortcuts import render, redirect
from .models import OrdenTrabajo
from .forms import OrdenTrabajoForm

def lista_ordenes(request):
    """Muestra el listado general de órdenes de trabajo para el control de turnos en la planta."""
    ordenes = OrdenTrabajo.objects.all().order_by('-creado_en')
    return render(request, 'ordentrabajo/lista.html', {'ordenes': ordenes})

def crear_orden(request):
    """Permite registrar una nueva orden correctiva o preventiva en el sistema."""
    if request.method == 'POST':
        form = OrdenTrabajoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ordentrabajo:lista_ordenes')
    else:
        form = OrdenTrabajoForm()
    return render(request, 'ordentrabajo/crear.html', {'form': form})
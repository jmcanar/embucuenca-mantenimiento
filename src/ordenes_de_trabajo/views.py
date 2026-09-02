from django.shortcuts import render, redirect
from .models import OrdenTrabajo
from .forms import OrdenTrabajoForm

def lista_ordenes(request):
    """Muestra el listado general de órdenes de trabajo."""
    ordenes = OrdenTrabajo.objects.all().order_by('-creado_en')
    return render(request, 'ordenes_de_trabajo/lista.html', {'ordenes': ordenes})

def crear_orden(request):
    """Permite registrar una nueva orden de trabajo."""
    if request.method == 'POST':
        form = OrdenTrabajoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ordenes_de_trabajo:lista_ordenes')
    else:
        form = OrdenTrabajoForm()
    return render(request, 'ordenes_de_trabajo/crear.html', {'form': form})
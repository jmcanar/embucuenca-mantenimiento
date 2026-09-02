from django.urls import path
from . import views

# Debe coincidir exactamente con el nombre de la carpeta de la app
app_name = 'ordenes_de_trabajo'

urlpatterns = [
    path('', views.lista_ordenes, name='lista_ordenes'),
    path('crear/', views.crear_orden, name='crear_orden'),
]
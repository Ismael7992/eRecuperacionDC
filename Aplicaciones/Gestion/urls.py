from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('pilotos/', views.listadoPilotos, name='listadoPilotos'),
    path('pilotos/nuevo/', views.nuevoPiloto, name='nuevoPiloto'),
    path('pilotos/guardar/', views.guardarPiloto, name='guardarPiloto'),
    path('pilotos/editar/<int:id>/', views.editarPiloto, name='editarPiloto'),
    path('pilotos/actualizar/', views.procesarActualizacionPiloto, name='actualizarPiloto'),
    path('pilotos/eliminar/<int:id>/', views.eliminarPiloto, name='eliminarPiloto'),


    path('aviones/', views.listadoAviones, name='listadoAviones'),
    path('aviones/nuevo/', views.nuevoAvion, name='nuevoAvion'),
    path('aviones/guardar/', views.guardarAvion, name='guardarAvion'),
    path('aviones/editar/<int:id>/', views.editarAvion, name='editarAvion'),
    path('aviones/actualizar/', views.procesarActualizacionAvion, name='actualizarAvion'),
    path('aviones/eliminar/<int:id>/', views.eliminarAvion, name='eliminarAvion'),
]

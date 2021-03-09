from django.contrib import admin
from django.urls import path

from . import views

app_name = "proyecto_app"

urlpatterns = [
    path('proyectolista',views.VistaProyectos.as_view(),name="lista"),
    path('categoria/<nombre>/',views.VistaxCategoria.as_view(),name="listacategoria"),
    path('detalle/<pk>/',views.ProyectoDetailView.as_view(),name="detalle"),
    path('crearproyecto/',views.ProyectoCreateView.as_view(),name="crear"),
]
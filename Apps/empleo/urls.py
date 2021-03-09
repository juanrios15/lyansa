from django.contrib import admin
from django.urls import path

from . import views

app_name = "empleo_app"

urlpatterns = [
    path('empleo',views.VistaEmpleos.as_view(),name="empleo"),
    path('categoriaempleos/<nombre>/',views.VistaEmpleosxCat.as_view(),name="empleocategoria"),
    path('crearempleo',views.EmpleoCreateView.as_view(),name="crearempleo"),
]
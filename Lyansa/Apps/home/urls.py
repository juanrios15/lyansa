from django.contrib import admin
from django.urls import path

from . import views

app_name = "home"

urlpatterns = [
    path('',views.HomePage.as_view(),name="inicio"),
    path('registro',views.RegisterUser.as_view(),name="registro"),
    path('login',views.LoginUser.as_view(),name="login"),
    path('logout',views.LogoutUser.as_view(),name="logout"),
    path('formulario',views.ContactView.as_view(),name="formulario"),
    path('formulario/<slug>',views.ContactView.as_view(),name="formulario2"),
    path('servicios',views.ServiciosView.as_view(),name="servicios"),
    path('contacto',views.ContactoView.as_view(),name="contacto"),
    path('filosofia',views.FilosofiaView.as_view(),name="filosofia"),
    path('infolegal',views.InfoLegalView.as_view(),name="infolegal"),
    path('politicas',views.PoliticasView.as_view(),name="politicas"),
       
]
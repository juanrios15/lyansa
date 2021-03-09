from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
# Create your views here.

from .models import Empleo

from .forms import CrearEmpleoForm

class VistaEmpleos(ListView):
    
    model = Empleo
    template_name= "empleo/lista.html"
    queryset = Empleo.objects.filter(publico=True).order_by("-created_at")
    paginate_by = 6
    context_object_name= "empleo"

class VistaEmpleosxCat(ListView):
    model = Empleo
    context_object_name= "empleo"
    template_name= "empleo/categoriasemp.html"
    
    def get_queryset(self):
        categoria = self.kwargs['nombre']
        lista = Empleo.objects.filter(Categories__nombre=categoria,publico=True).order_by("-created_at")
        return lista
    
    def get_context_data(self, **kwargs):
        dpto = self.kwargs['nombre']
        context = super().get_context_data(**kwargs)
        context["dpto"] = dpto
        return context

class EmpleoCreateView(LoginRequiredMixin,CreateView):

    form_class= CrearEmpleoForm
    template_name = "empleo/crear.html"
    success_url = reverse_lazy("empleo_app:empleo")
    success_message = "Oferta de empleo registrada correctamente!"
    
    def form_valid(self,form):

        form.instance.user = self.request.user

        return super(EmpleoCreateView,self).form_valid(form)
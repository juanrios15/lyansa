from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.messages.views import SuccessMessageMixin 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


from .models import Proyecto
from .forms import CrearProyectoForm
# Create your views here.

class VistaProyectos(ListView):
    
    model = Proyecto
    template_name= "proyectos/lista.html"
    queryset = Proyecto.objects.filter(publico=True).order_by("-created_at")
    paginate_by = 4
    context_object_name= "proyectos"

class VistaxCategoria(ListView):
    model = Proyecto
    context_object_name= "proyectos"
    template_name= "proyectos/categorias.html"
    
    def get_queryset(self):
        categoria = self.kwargs['nombre']
        lista = Proyecto.objects.filter(Categories__nombre=categoria,publico=True).order_by("-created_at")
        return lista
    
    def get_context_data(self, **kwargs):
        dpto = self.kwargs['nombre']
        context = super().get_context_data(**kwargs)
        context["dpto"] = dpto
        return context

class ProyectoDetailView(DetailView):
    
    model = Proyecto
    template_name = "proyectos/detalle.html"

class ProyectoCreateView(LoginRequiredMixin,CreateView):

    form_class= CrearProyectoForm
    template_name = "proyectos/crear.html"
    success_url = reverse_lazy("proyecto_app:lista")
    success_message = "Proyecto Registrado correctamente!"
    
    def form_valid(self,form):

        form.instance.user = self.request.user

        return super(ProyectoCreateView,self).form_valid(form)

    
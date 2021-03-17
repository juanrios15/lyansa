from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


from .models import Proyecto, Foto
from .forms import CrearProyectoForm, AgregarImagenForm
from django.contrib import messages
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
        lista = Proyecto.objects.filter(Categories__nombre=categoria,publico=True).order_by("-updated_at")
        return lista
    
    def get_context_data(self, **kwargs):
        dpto = self.kwargs['nombre']
        context = super().get_context_data(**kwargs)
        context["dpto"] = dpto
        return context

class ProyectoDetailView(TemplateView):
    
    template_name = "proyectos/detalle.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['proyecto'] = Proyecto.objects.get(id=self.kwargs['pk'])
        
        context['galeria'] = Foto.objects.fotos_proyecto(self.kwargs['pk'])
        
        return context
           

class ProyectoCreateView(LoginRequiredMixin,CreateView):

    form_class= CrearProyectoForm
    template_name = "proyectos/crear.html"
    success_url = reverse_lazy("proyecto_app:lista")
    success_message = "Proyecto Registrado correctamente!"
    
    def form_valid(self,form):

        form.instance.user = self.request.user

        return super(ProyectoCreateView,self).form_valid(form)

class ProyectoUpdateView(LoginRequiredMixin,UpdateView):
    
    model = Proyecto
    template_name= "proyectos/editar.html"
    form_class= CrearProyectoForm
    success_url = reverse_lazy('proyecto_app:lista')
    
    def form_valid(self, form):
      messages.success(self.request, "Proyecto editado con exito")
      return super().form_valid(form)



class AgregarImagenView(LoginRequiredMixin,CreateView):

    form_class= AgregarImagenForm
    template_name = "proyectos/agregar_imagen.html"
    success_url = reverse_lazy("proyecto_app:lista")
    success_message = "Imagen agregada correctamente!"
    
    def form_valid(self,form):

        form.instance.user = self.request.user

        return super(AgregarImagenView,self).form_valid(form)
    
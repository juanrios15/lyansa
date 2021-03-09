from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin 
from django.contrib.auth import authenticate, login, logout ###
from django.urls import reverse_lazy, reverse ###
from django.contrib import messages ###
from django.views.generic import TemplateView, CreateView, View, ListView ###
from django.views.generic.edit import FormView ###
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage

from .forms import RegisterForm, LoginForm, ContactForm ###

from Apps.proyectos.models import Proyecto
from .models import Servicio



# Create your views here.

class HomePage(TemplateView):
    template_name = "home/inicio.html"
    
    def get_context_data(self, **kwargs):
        context = super(HomePage,self).get_context_data(**kwargs)

        context["home"] = Proyecto.objects.proyecto_principal()
        context["portadas"] = Proyecto.objects.entradas_recientes()

        #context["portadas"] = Entry.objects.entrada_en_portada() 
        #contexto para los articulos de home

        return context

class RegisterUser(SuccessMessageMixin,CreateView):
    
    form_class= RegisterForm
    template_name = "home/register.html"
    success_url = "/"
    success_message = "Registrado correctamente, bienvenido!"
    
#####
class LoginUser(SuccessMessageMixin,FormView):
    template_name = 'home/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home:inicio')
    success_message = "Login Exitoso! Bienvenido"
    
    def form_valid(self,form):

        user= authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        
        return super(LoginUser,self).form_valid(form)
    
class LogoutUser(SuccessMessageMixin,View):
        
    def get(self, request, *args, **kargs):
        messages.success(request, 'Hasta Pronto!!!')
        
        logout(request)

        return HttpResponseRedirect(
            reverse(
                'home:inicio'
            )
        )

class ContactView(SuccessMessageMixin,FormView):
    
    template_name = 'home/formulario.html'
    form_class = ContactForm
    success_url = reverse_lazy('home:inicio')
    success_message = "Formulario enviado correctamente, gracias!"
    
    def setup(self, request, *args, **kwargs):

        self.request = request
        self.args = args
        self.kwargs = kwargs
        
    
    def form_valid(self,form):
        
        asunto = form.cleaned_data['asunto']
        nombre = form.cleaned_data['nombre']
        email = form.cleaned_data['email']
        attach = form.cleaned_data['adjunto']

        m = form.cleaned_data['mensaje']
        mensaje = "Nombre: "+ str(nombre)+"\nEmail: " + str(email)
        
        mensaje_html = f"""
                    <h1> Formulario de contacto </h1>
                    <h2> Asunto:  {asunto}  </h2>
                    <h3> Nombre:  {nombre}  </h3> 
                    <h3> Email: {email}  </h3> 
                    <p> {m}  </p> 
                """
        
        envio_email = EmailMessage(asunto,mensaje_html,'juankrios15@gmail.com',('juankrios15@gmail.com',))
        envio_email.attach(attach.name,attach.read())
        envio_email.content_subtype = 'html'
        envio_email.send()
        
                
        return super().form_valid(form)
    
    
    def get_initial(self, **kwargs):
        
        try:
            asunto ="Cargo: " + str(self.kwargs['slug'])
            return { 'asunto': asunto, 'mensaje': 'Estoy interesado en su oferta laboral' }
        except:
            return { 'asunto': ""}
        
    


#########SERVICIOS

class ServiciosView(ListView):
    template_name = "home/servicios.html"
    model = Servicio
    context_object_name= "servicios"
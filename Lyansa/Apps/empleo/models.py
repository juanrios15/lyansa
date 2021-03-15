from django.db import models
from ckeditor.fields import RichTextField
from Apps.proyectos.models import Categoria
from django.contrib.auth.models import User

# Create your models here.
class Empleo(models.Model):
    
    titulo = models.CharField(verbose_name="Titulo", max_length=250)
    resumen = RichTextField(verbose_name="Resumen")
    Categories = models.ManyToManyField(Categoria, verbose_name="Categorias", blank=True, related_name="empleos")
    proyecto = models.CharField(verbose_name="Proyecto", max_length=250)
    ubicacion = models.CharField(verbose_name="Ubicacion", max_length=250, blank=True)
    duracion = models.CharField(verbose_name="Duración", max_length=250, blank=True)
    salario = models.CharField(verbose_name="Salario", max_length=50, blank=True)
    user = models.ForeignKey(User, verbose_name="Usuario", on_delete=models.CASCADE, editable=False)
    publico = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    updated_at= models.DateTimeField(auto_now=True, verbose_name="Actualizado el")
    
    class Meta:
        verbose_name= "Empleo"
        verbose_name_plural = "Empleos"
    
    def __str__(self):
        return self.titulo
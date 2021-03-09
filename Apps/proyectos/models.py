
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


from .managers import PortadasManager
# Create your models here.

class Categoria(models.Model):
    
    nombre = models.CharField(verbose_name="Categoria", max_length=100)
    descripcion = models.CharField(verbose_name="Descripcion", max_length=250)
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
    
    def __str__(self):
        return self.nombre
    

class Proyecto(models.Model):
    
    nombre = models.CharField(max_length=150,verbose_name="Titulo")
    year = models.IntegerField(verbose_name="Año")
    resumen = models.CharField(verbose_name="Resumen", max_length=250)
    Categories = models.ManyToManyField(Categoria, verbose_name="Categorias", blank=True, related_name="articulos")
    descripcion = RichTextField(verbose_name="Descripcion",blank=True)
    imagen = models.ImageField(upload_to="media", height_field=None, width_field=None, max_length=None,blank=True)
    user = models.ForeignKey(User, verbose_name="Usuario", on_delete=models.CASCADE, editable=False)
    publico = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    updated_at= models.DateTimeField(auto_now=True, verbose_name="Actualizado el")
    
    objects = PortadasManager()
    
    
    class Meta:
        verbose_name= "Proyecto"
        verbose_name_plural = "Proyectos"
    
    def __str__(self):
        return self.nombre
# Create your models here.from django.db import models

# Create your models here.


    
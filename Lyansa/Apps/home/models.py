from django.db import models
# Create your models here.
from ckeditor.fields import RichTextField


class Servicio(models.Model):
    titulo= models.CharField(verbose_name="Titulo", max_length=150)
    resumen = RichTextField(verbose_name="Resumen")
    imagen =  models.ImageField(upload_to="media", height_field=None, width_field=None, max_length=None,blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    updated_at= models.DateTimeField(auto_now=True, verbose_name="Actualizado el")
    
    
    class Meta:
        verbose_name= "Servicio"
        verbose_name_plural = "Servicios"
    
    def __str__(self):
        return self.titulo
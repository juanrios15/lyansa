from django.db import models

class PortadasManager(models.Manager):
    
    def proyecto_principal(self):
        return self.filter(
            publico=True
        ).order_by('-created_at').first()
    
    def entradas_recientes(self):
        return self.filter(
            publico = True,

        ).order_by('-created_at')[1:5]


class FotosManager(models.Manager):
    def fotos_proyecto(self,id):
        return self.filter(
            proyecto__id=id)
    
from django.contrib import admin

from .models import Servicio

# Register your models here.
admin.site.site_header = "Panel administrativo - Lyansa"
admin.site.site_title = "Lyansa Electrica"
admin.site.index_title = "Panel principal"

admin.site.register(Servicio)
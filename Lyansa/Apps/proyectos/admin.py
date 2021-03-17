from django.contrib import admin

from .models import Proyecto, Categoria, Foto

class mipanel(admin.ModelAdmin):
    
    readonly_fields = ("user","created_at","updated_at")
    search_fields = ("nombre","resumen","user__username","Categories__nombre")
    list_filter = ("publico","Categories__nombre",)
    list_display = ('nombre','resumen','created_at','user','publico')
    ordering = ("-created_at",)
    
    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id
        obj.save()


admin.site.register(Proyecto, mipanel)
admin.site.register(Categoria)
admin.site.register(Foto)
from django.contrib import admin
from aplicacion.models import Cliente


class ClienteAdmin(admin.ModelAdmin):
    list_display = ['rut','nombre','correo','direccion','telefono','numeroCompras']
    
# Register your models here.
admin.site.register(Cliente)
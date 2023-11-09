from django.db import models

# Create your models here.
class Cliente(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=20)
    correo = models.EmailField()
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    numeroCompras = models.IntegerField(default=0)



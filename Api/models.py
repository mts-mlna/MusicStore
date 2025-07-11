from django.db import models
from ckeditor.fields import RichTextField

# Create your models here
class Producto(models.Model):
    Codigo = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Descripcion = models.TextField()
    Precio = models.DecimalField(max_digits=10, decimal_places=2)
    Stock = models.IntegerField()
    Imagen = models.ImageField(upload_to="Musimg", null=True)

    def __int__(self):
        return self.Codigo

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
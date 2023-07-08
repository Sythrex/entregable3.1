from django.db import models

# Create your models here.

#Modelo para la Categoria
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCatgoria = models.CharField(max_length=50, verbose_name='Nombre de la Categoría')
    def __str__(self):
        return self.nombreCatgoria

#Modelo para el Vehiculo
class Vehiculo(models.Model):
    patente = models.CharField(max_length=25, primary_key=True, verbose_name='Nombre Mecanico')
    marca = models.CharField(max_length=25, verbose_name='Atención Realizada')
    modelo = models.CharField(max_length=10, null=True, verbose_name='Fecha de Atención')
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    def __str__(self):
        return self.patente

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name
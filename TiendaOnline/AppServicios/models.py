from django.db import models

# Create your models here.

class Servicio(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='servicios')#La primer imagen va a crear la carpeta llamada servicios
    created=models.DateTimeField(auto_now_add=True)#Con el auto_now nos indica la fecha de creacion automaticamente
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:#Esto va a ser como va a estar almacenado en la base de datos
        verbose_name="servicio"
        verbose_name_plural="servicios"

    def __str__(self):
        return self.titulo
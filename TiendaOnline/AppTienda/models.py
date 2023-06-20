from django.db import models

# Create your models here.

class CategoriaArticulo(models.Model):
    nombre=models.CharField(max_length=55)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="categoria_Producto"
        verbose_name_plural="categorias_Productos"

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    nombre=models.CharField(max_length=50)
    categoria=models.ForeignKey(CategoriaArticulo, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='tienda', null=True, blank=True)
    precio=models.FloatField()
    disponible=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"

    def __str__(self):
        return "Articulo: %s Precio: %s" % (self.nombre, self.precio)
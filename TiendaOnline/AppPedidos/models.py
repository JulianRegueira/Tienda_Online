from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import F, Sum, FloatField
from AppTienda.models import Articulo

# Create your models here.

User=get_user_model() #Esta funcion devuelve el usuario activo en la sesion

class Pedido(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Pedido {self.id}"
    
    def calcular_monto_total(self):
        detalles = self.detallepedido_set.all()
        return sum(detalle.cantidad * detalle.precio for detalle in detalles)
    
    @property
    def total(self):
        return self.detallepedido_set.aggregate(
            total=Sum(F("precio") * F("cantidad"), output_field=FloatField())
        )["total"]

    class Meta:
        db_table='Pedidos'
        verbose_name='Pedido'
        verbose_name_plural='Pedidos'
        ordering=['id']

class DetallePedido(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    producto=models.ForeignKey(Articulo, on_delete=models.CASCADE)
    pedido=models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad=models.IntegerField(default=1)
    precio=models.FloatField(editable=False)
    precio_al_momento = models.FloatField()
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.cantidad} unidades de {self.producto.nombre}'
    
    class Meta:
        db_table='DetallePedidos'
        verbose_name='DetallePedido'
        verbose_name_plural='DetallePedidos'
        ordering=['id']
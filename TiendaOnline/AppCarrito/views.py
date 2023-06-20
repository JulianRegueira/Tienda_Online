from django.shortcuts import redirect
from .carro import Carro
from AppTienda.models import Articulo

# Create your views here.

def agregar_producto(request, producto_id):

    carro=Carro(request)

    producto=Articulo.objects.get(id=producto_id)

    carro.agregar(producto=producto)

    return redirect("Tienda")

def eliminar_producto(request, producto_id):

    carro=Carro(request)

    producto=Articulo.objects.get(id=producto_id)

    carro.eliminar(producto=producto)

    return redirect("Tienda")

def restar_producto(request, producto_id):

    carro=Carro(request)

    producto=Articulo.objects.get(id=producto_id)

    carro.restar_producto(producto=producto)

    return redirect("Tienda")

def vaciar_carro(request, producto_id):

    carro=Carro(request)

    carro.vaciar_carro()

    return redirect("Tienda")
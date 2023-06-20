from django.shortcuts import render
from .models import Articulo

def tienda(request):

    articulos=Articulo.objects.all() #Traigo todos los objetos en Articulo

    return render(request, "Tienda/tienda.html", {"articulos":articulos}) #Muestro todos los articulos
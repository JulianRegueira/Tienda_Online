from django.http import HttpResponse
from django.shortcuts import render
from AppTienda.models import Articulo

# Create your views here.

def index(request):
    return render(request, "index.html")

def buscar_producto(request):

    return render(request, "BarraPrincipal/Buscador/buscar_producto.html")

def buscar(request):

    if request.GET["buscar"]: #Se llama por ID indicado en el html buscar_producto.html

        articulo_buscado=request.GET["buscar"] #Rescatamos la info que introdujo el usuario

        if len(articulo_buscado)>20:
            
            mensaje="Debes ser mas breve."

        else:

            articulos=Articulo.objects.filter(nombre__icontains=articulo_buscado)

            return render(request, "BarraPrincipal/Buscador/resultado_busqueda.html", {"articulos":articulos, "query":articulo_buscado})

    else:
        return render(request, "BarraPrincipal/Buscador/busqueda_vacia.html")

    return HttpResponse(mensaje)

def preguntas(request):

    return render(request, "Faqs/preguntas.html")

from django.shortcuts import render

def politicas_privacidad(request):
    return render(request, 'Footer/politicasprivacidad.html')

def aviso_legal(request):
    return render(request, 'Footer/avisolegal.html')

def cookies(request):
    return render(request, 'Footer/cookies.html')

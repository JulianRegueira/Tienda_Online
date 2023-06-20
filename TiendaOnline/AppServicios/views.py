from django.shortcuts import render
from AppServicios.models import Servicio

# Create your views here.

def servicios(request):
    #Importamos la lista de servicios que hay en el panel y la mostramos en el html indicado
    servicios=Servicio.objects.all()#Le digo a Django que importe todos los servicios que se encuentren

    return render(request, "Barra Principal\servicios.html", {"servicios":servicios})#Con este DICT le decimos que cargue todos los servicios que hay
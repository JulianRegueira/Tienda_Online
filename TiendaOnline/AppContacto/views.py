from django.shortcuts import render
from django.core.mail import send_mail
from AppContacto.forms import Formulario_Contacto

# Create your views here.

def contacto(request):

    if request.method=="POST":

        miFormulario=Formulario_Contacto(request.POST)

        if miFormulario.is_valid():

            #Si el formulario es valido, hay que crear una variable donde almacenar la info que se ingreso, en este caso la llame formularioFinal
            formularioFinal=miFormulario.cleaned_data

            send_mail(formularioFinal["asunto"], formularioFinal["mensaje"],
            formularioFinal.get("email",""),["julian_regueira@hotmail.com"],)

            return render (request, "Contacto/gracias.html")
        
    else:

        miFormulario=Formulario_Contacto()

    return render(request, "Contacto/Form_Contacto.html", {"form":miFormulario})

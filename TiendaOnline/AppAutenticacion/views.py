from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

######################################################################################
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm
from AppPedidos.models import Pedido

# Create your views here.
        
def cerrar_sesion(request):
    logout(request)

    return redirect('Index')

def logearse(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            contraseña=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=contraseña) #El metodo autenticate comprueba si el usuario y pw coincide
            if usuario is not None:
                login(request, usuario)
                return redirect('Index')
            
            else:
                messages.error(request,"Usuario no valido")

        else:
            messages.error(request,"Algo está mal")
   
    form=AuthenticationForm()

    return render(request, "Login/login.html", {"form":form})


class SignupView(CreateView):

    form_class = SignUpForm
    success_url = reverse_lazy("Index")
    template_name = "Registro/registro.html"

def mostrar_pedidos(request):
    # Obtener el usuario actual
    user = request.user

    # Obtener todos los detalles de los pedidos del usuario
    pedidos = Pedido.objects.filter(user=user)

    # Pasar los detalles de los pedidos al template HTML
    return render(request, 'Perfil/mostrar_pedidos.html', {'pedidos': pedidos})
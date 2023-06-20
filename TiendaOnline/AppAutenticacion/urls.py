from django.urls import path
from AppAutenticacion import views
from .views import cerrar_sesion, logearse

urlpatterns = [
    path('', views.SignupView.as_view(), name="Registro"), #Mostrando clase como vista
    path('cerrar_sesion', cerrar_sesion, name="Cerrar_sesion"),
    path('login', logearse, name="Login"),
]

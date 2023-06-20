"""
URL configuration for TiendaOnline project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("AppWeb.urls")), #Incluimos todos los URLS de nuestras APPS
    path('servicios/', include('AppServicios.urls')),
    path('contacto/', include('AppContacto.urls')),
    path('tienda/', include('AppTienda.urls')),
    path('carro/', include('AppCarrito.urls')),
    path('autenticacion/', include('AppAutenticacion.urls')),
    path('pedidos/', include('AppPedidos.urls')),
]

from django.urls import path
from AppContacto import views

urlpatterns = [
    path('', views.contacto, name="Contacto"),
]

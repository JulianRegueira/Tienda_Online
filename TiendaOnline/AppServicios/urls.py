from django.urls import path
from AppServicios import views

urlpatterns = [
    path("", views.servicios, name="Servicios"),
]
from django.urls import path
from AppTienda import views

urlpatterns = [
    path("", views.tienda, name="Tienda"),
]
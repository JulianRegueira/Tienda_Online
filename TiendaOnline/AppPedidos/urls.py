from django.urls import path
from AppPedidos import views

urlpatterns = [
    path("", views.procesar_pedido, name="procesar_pedido"),
    path('calcular_monto_pedido/<int:id_pedido>/', views.calcular_monto_pedido, name='calcular_monto_pedido'),
]
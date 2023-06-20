from django.urls import path
from AppWeb import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="Index"),
    path("buscar_producto/", views.buscar_producto, name="Buscar_Producto"),
    path("buscar/", views.buscar),
    path("preguntas/", views.preguntas, name="Preguntas"),
    path('politicasprivacidad/', views.politicas_privacidad, name="Politicas_privacidad"),
    path('aviso_legal/', views.aviso_legal, name="Aviso_legal"),
    path('cookies/', views.cookies, name="Cookies"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #Con esta cfg podemos mostrar las imagenes de servicios desde el panel de admin
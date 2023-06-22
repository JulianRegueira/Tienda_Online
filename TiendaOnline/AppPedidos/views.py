from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from AppPedidos.models import Pedido, DetallePedido
from AppCarrito.carro import Carro
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

from AppTienda.models import Articulo

# Create your views here.

@login_required(login_url='autenticacion/')
def procesar_pedido(request):
    # Se da de alta el pedido
    pedido = Pedido.objects.create(user=request.user)
    carro = Carro(request)
    lineas_pedido = []

    for key, value in carro.carro.items():
        # Obtener el precio del producto al momento de hacer el pedido
        producto = Articulo.objects.get(id=key)
        precio = producto.precio

        # Crear el objeto DetallePedido con el precio obtenido
        detalle_pedido = DetallePedido(
            producto_id=key,
            cantidad=value["cantidad"],
            precio_al_momento=precio, # guardar el precio al momento
            precio=precio,  # guardar el precio en el objeto DetallePedido
            user=request.user,
            pedido=pedido,
        )
        lineas_pedido.append(detalle_pedido)

    DetallePedido.objects.bulk_create(lineas_pedido)

    enviar_mail(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombre_usuario=request.user.username,
        email_usuario=request.user.email,
    )

    return render(request, 'Pedidos/procesado.html', {'pedido': pedido})


def enviar_mail(**kwargs):

    asunto="Gracias por tu pedido"

    #La info del mensaje se rescata del proceso del pedido
    mensaje=render_to_string("Emails/pedido.html",{
        "pedido": kwargs.get("pedido"),
        "lineas_pedido": kwargs.get("lineas_pedido"),
        "nombre_usuario": kwargs.get("nombre_usuario"),

    })

    mensaje_texto=strip_tags(mensaje)
    from_email="worldofjuli2@gmail.com" #IMPORTANTE ESTE CAMPO, es QUIEN envia el mail
    to=kwargs.get("email_usuario")

    send_mail(asunto, mensaje_texto, from_email, [to], html_message=mensaje)

def calcular_monto_pedido(request, external_reference):

    # Busco el pedido en la BD
    pedido = Pedido.objects.get(external_reference=external_reference)
    
    monto_total = pedido.calcular_monto_total()

    return monto_total
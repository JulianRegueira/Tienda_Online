from django.contrib import admin
from .models import Pedido, DetallePedido

# Register your models here.

class DetallePedidoInline(admin.TabularInline):
    model = DetallePedido
    extra = 1

class PedidoAdmin(admin.ModelAdmin):
    inlines = [DetallePedidoInline]
    list_display = ('id', 'user', 'fecha', 'productos', 'total')

    def fecha(self, obj):
        return obj.created_at.strftime('%d/%m/%Y')
    
    def productos(self, obj):
        detalles = obj.detallepedido_set.all()
        productos_info = []
        for detalle in detalles:
            producto = detalle.producto
            cantidad = detalle.cantidad
            precio_unitario = producto.precio
            precio_total = cantidad * precio_unitario
            productos_info.append(f"{producto.nombre} ({cantidad} unidades x ${precio_unitario} c/u = ${precio_total})")
        return ", ".join(productos_info)

    def total(self, obj):
        if obj.total is not None:
            return f"${obj.total:.2f}"
        else:
            return ""


    fecha.admin_order_field = 'created_at'
    productos.short_description = 'Productos'
    total.short_description = 'Total'

admin.site.register(Pedido, PedidoAdmin)
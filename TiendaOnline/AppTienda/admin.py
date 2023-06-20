from django.contrib import admin
from AppTienda.models import Articulo, CategoriaArticulo
# Register your models here.

class CategoriaArtAdmin(admin.ModelAdmin):

    readonly_fields=("created", "updated")

class ArticuloAdmin(admin.ModelAdmin):

    readonly_fields=("created", "updated")

admin.site.register(CategoriaArticulo, CategoriaArtAdmin)
admin.site.register(Articulo,ArticuloAdmin)
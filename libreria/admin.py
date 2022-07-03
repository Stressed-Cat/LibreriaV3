from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Ciudad)
admin.site.register(Idioma)
admin.site.register(Genero)
admin.site.register(Editorial)
admin.site.register(Tipo)
admin.site.register(Articulo)
admin.site.register(Compra)
admin.site.register(Ejemplar)
# Carrito
admin.site.register(Orden)
admin.site.register(OrdenItem)
admin.site.register(DireccionEntrega)
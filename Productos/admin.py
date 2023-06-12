from django.contrib import admin
from Productos.Articulos_Venta import Articulos_Venta
from Productos.Eventos import Eventos
from Productos.Pedidos import Pedidos
from Productos.Reservas import Reservas
# Register your models here.
admin.site.register(Articulos_Venta)
admin.site.register(Eventos)
admin.site.register(Pedidos)
admin.site.register(Reservas)
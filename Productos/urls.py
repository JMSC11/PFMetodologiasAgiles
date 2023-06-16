from django.contrib import admin
from django.urls import path, include
from cuenta import views
from . import views



urlpatterns = [
   path('Nueva_Reserva/<id>', views.Nueva_Reserva, name='nueva_reserva'),   
   path('Ver_Pedidos/', views.Ver_Pedidos, name='Ver_Pedidos'),
   path('Cancelar_Pedido/<id>', views.Cancelar_Pedido, name = "Cancelar_Pedido"),
   path('Ver_Reservas/', views.Ver_Reservas, name="Ver_Reservas"),
   path('Cancelar_Reserva/<id>', views.Cancelar_Reserva, name = "Cancelar_Reserva"),
]

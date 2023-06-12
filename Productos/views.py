
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from cuenta.Barista import Barista
from Productos.Articulos_Venta import Articulos_Venta
from Productos.Pedidos import Pedidos


# Create your views here.

def nuevo_Pedido(request):
    articulos_venta = Articulos_Venta.objects.all()
    pedido=[]   
    for elem in articulos_venta:
        nombre_campo = str(elem.id)
        cantidad = request.POST[nombre_campo]
        print(cantidad)

        if int(cantidad) > 0:
            articulo = (elem.nombre, cantidad)
            pedido.append(articulo)
    print("El pedido es:")
    print(pedido)
    total = getTotal(pedido)
    user = request.user

    nuevo_pedido = Pedidos.objects.create(productos = pedido,
                                          total = total,
                                          is_active = True,
                                          id_cliente = user)
    nuevo_pedido.save()

def getTotal(pedido):
    total = 0
    for elem in pedido:
        #elem tupla [articulo, cantidad]
        articulo = Articulos_Venta.objects.filter(nombre = elem[0])
        for i in articulo:
            print(i.nombre)
            total += i.precio * int(elem[1])
    return total


"""TODO: Backend para agregar una nueva reservación.
    @user: cliente
    PASO 1. Modificar el html "lista_eventos" - ve a lista_eventos
    PASO 2. Crear una funcion en éste archivo DE NOMBRE Nueva_Reserva

    def Nueva_Reserva(request, id):
        if metodo es get:
        
        else
            ¿que se necesita?
            id_cliente = request.user
            id_evento = id
            is_active = True

            reserva = Reservas.objects.create(id_cliente, .....)
            reserva.save
            return render(request, 'home.html')
"""
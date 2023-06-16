
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from cuenta.Barista import Barista
from Productos.Articulos_Venta import Articulos_Venta
from Productos.Pedidos import Pedidos
from Productos.Reservas import Reservas
from Productos.Eventos import Eventos

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


def Nueva_Reserva(request, id):
    #    evento = models.ForeignKey(Eventos, on_delete= models.CASCADE)
    #is_active = models.BooleanField()
    #id_cliente = models.ForeignKey(User, on_delete = models.CASCADE)
    evento = Eventos.objects.get(pk = id)
    user = request.user
    print(user)
    reserva = Reservas.objects.create(id_cliente = user,
                                      evento = evento,
                                      is_active = True)
    reserva.save()
    lista_eventos = Eventos.objects.all()
    return render(request, 'lista_eventos.html', {'lista_eventos' : lista_eventos})
    #nueva_reserva = Reservas.objects.create(id)

def Ver_Pedidos(request): 
    user = request.user
    lista_pedidos = Pedidos.objects.filter(id_cliente=user, is_active = True)
    print(lista_pedidos)
    return render(request, 'VerPedidos.html', {'lista_pedidos' : lista_pedidos})

def Cancelar_Pedido(request, id):
    user = request.user
    pedido = Pedidos.objects.get(pk = id)
    pedido.is_active = False
    pedido.save()
    lista_pedidos = Pedidos.objects.filter(id_cliente=user, is_active = True)    
    return render(request, 'VerPedidos.html', {'lista_pedidos' : lista_pedidos})

def Ver_Reservas(request): 
    user = request.user
    lista_reservas = Reservas.objects.filter(id_cliente=user, is_active = True)
    print(lista_reservas)
    return render(request, 'ver_reserva_cliente.html', {'lista_reservas' : lista_reservas})

def Cancelar_Reserva(request, id):
    user = request.user
    reserva = Reservas.objects.get(pk = id)
    reserva.is_active = False
    reserva.save()
    lista_reservas = Reservas.objects.filter(id_cliente=user, is_active = True)    
    return render(request, 'ver_reserva_cliente.html', {'lista_reservas' : lista_reservas})

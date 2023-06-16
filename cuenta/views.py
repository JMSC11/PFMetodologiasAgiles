from http.client import HTTPResponse

import django.http
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
import logging
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.contrib import messages
from .forms import CustomUserCreationForm
from .forms import RegistroCuenta
from cuenta.Barista import Barista
from Productos.Articulos_Venta import Articulos_Venta
from Productos.Eventos import Eventos
from Productos.views import nuevo_Pedido
# Create your views here.

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    
@login_required
def home(request):
    usuario = request.user.username
    id_user = request.user.id
    articulos_venta = Articulos_Venta.objects.all()
    if request.method == 'GET':
        if usuario == 'admin':
            return redirect("/admin/")
        else:
            try:
                barista = Barista.objects.get(user = id_user)
                if barista.isBarista == True:
                    return render(request, 'homebarista.html')
            except:
                return render(request, 'home.html', {'articulos_venta' : articulos_venta})
    else: #request.method == 'POST'
        print("Presione boton")
        print(request.POST)
        try:
            barista = Barista.objects.get(user = id_user)
            if barista.isBarista == True:
                print("accion del barista")           
        except:
            # Manejar otras excepciones
            nuevo_Pedido(request)
                
        return render(request, 'home.html',{'articulos_venta' : articulos_venta})
        
        

def register(request):
    data = {
        'form' : CustomUserCreationForm()
    }
    if request.method == 'GET':
        print(request.GET)
        return render(request, 'registration/register.html', data)
    else:
        try:
            user_creation_form = CustomUserCreationForm(data=request.POST)
            if user_creation_form.is_valid():
                user_creation_form.save()
                #user = authenticate(username=user_creation_form.cleaned_data['username'], password = user_creation_form.cleaned_data['password1'])
                #login(request, user)
                return redirect('home')
        except Exception as e:
            logging.exception(e)
            print(e)
            return HttpResponse('Error al agregar proyecto 3')

def exit(request):
    logout(request)
    return redirect('index')

def lista_eventos(request):
    if request.method == 'GET':
        lista_eventos = Eventos.objects.all()
        return render(request, 'lista_eventos.html', {'lista_eventos' : lista_eventos})
    else:
        print("algo")
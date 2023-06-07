#from django.contrib.auth import login, logout
from django.contrib.auth.views import logout_then_login,LoginView
from django.contrib import admin
from django.urls import path, include
from cuenta import views
from . import views



urlpatterns = [
    path('', views.index, name='index'),   
    path('home/', views.home, name='home'),
    path('register/', views.register, name= 'register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', views.exit, name = 'exit' ),
    path('admin/', views.home, name='admin'),
    path('lista_eventos/', views.lista_eventos, name='lista_eventos'),
]

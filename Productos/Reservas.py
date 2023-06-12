from django.db import models
from django.contrib.auth.models import User
from Productos.Eventos import Eventos

class Reservas(models.Model):
    evento = models.ForeignKey(Eventos, on_delete= models.CASCADE)
    is_active = models.BooleanField()
    id_cliente = models.ForeignKey(User, on_delete = models.CASCADE)


    def __str__(self):
        return "Evento: " + str(self.evento) + "Cliente: " + str(self.id_cliente)

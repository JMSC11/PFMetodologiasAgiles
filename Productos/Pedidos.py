from django.db import models
from django.contrib.auth.models import User

class Pedidos(models.Model):
    productos = models.CharField(max_length=500)
    total = models.FloatField()
    is_active = models.BooleanField()
    id_cliente = models.ForeignKey(User, on_delete = models.CASCADE)


    def __str__(self):
        return "Pedido: " +  str(self.id) + " Cliente: " + str(self.id_cliente)

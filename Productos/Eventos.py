from django.db import models
from cuenta.Barista import Barista

class Eventos(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=300)
    fecha = models.DateField()
    barista = models.ForeignKey(Barista, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.nombre}"    
from django.db import models

# Create your models here.
class Articulos_Venta(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()

    def __str__(self):
        return f"{self.nombre}"   
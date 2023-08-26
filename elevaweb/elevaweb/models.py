from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    mensaje = models.CharField(max_length=2000)

    def __str__(self):
        return self.nombre, self.email
    
class Correo(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
    
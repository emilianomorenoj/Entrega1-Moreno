from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class RiderInfo(models.Model):

    def __str__(self):

        return f"Nombre: {self.name} ------- Fecha de nacimiento: {self.dateofbirth} ------- Email: {self.email}"

    name = models.CharField(max_length=60)
    dateofbirth = models.DateField()
    email = models.EmailField()


class Bikeinfo(models.Model):

    biketype = models.CharField(max_length=60)
    wheelsize = models.CharField(max_length=60)

class RacingEvent(models.Model):

    racingevent = models.CharField(max_length=60)
    racelevel = models.CharField(max_length=60)
    imagen = models.ImageField(upload_to = 'avatares', null=True)

class Avatar(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
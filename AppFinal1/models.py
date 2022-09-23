from django.db import models

# Create your models here.

class RiderInfo(models.Model):

    name = models.CharField(max_length=60)
    dateofbirth = models.DateField()
    email = models.EmailField()


class Bikeinfo(models.Model):

    biketype = models.CharField(max_length=60)
    wheelsize = models.CharField(max_length=60)

class RacingEvent(models.Model):

    racingevent = models.CharField(max_length=60)
    racelevel = models.CharField(max_length=60)


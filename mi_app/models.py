from mailbox import NoSuchMailboxError
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField

# Create your models here.

class familiares(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    edad = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}, {self.direccion}, {self.edad}"

class futbolistas(models.Model):
    nombre = models.CharField(max_length=200)
    edad = models.IntegerField()
    equipo = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}, {self.edad}, {self.equipo}"


class Autos(models.Model):
    modelo = models.CharField(max_length=200)
    marca = models.CharField(max_length=200)
    año = models.IntegerField()

    def __str__(self):
        return f"{self.modelo}, {self.marca}, {self.año}"
        

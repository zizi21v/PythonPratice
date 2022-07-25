from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models

class familyInfo(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    cumpleaños = models.DateField()
    
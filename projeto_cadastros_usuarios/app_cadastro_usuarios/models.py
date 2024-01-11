from django.db import models
from phone_field import PhoneField

# Create your models here.

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    name = models.TextField(blank=True)
    sobrenome = models.TextField(blank=True)
    nascimento = models.DateField(blank=True)
    phone = models.CharField(max_length=16, blank=True)
    email = models.EmailField(blank=True)


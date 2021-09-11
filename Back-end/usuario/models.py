from django.db import models
from persona.models import Persona
from base.models import BaseModel
# Create your models here.
class usuario(BaseModel):
    correoUsuario = models.CharField(max_length=200)
    contrasenaUsuario = models.CharField(max_length=200)
    Persona = models.ForeignKey(Persona, on_delete=models.CASCADE, verbose_name = 'inidicador de persona')
    def __str__(self):
        return '{}'.format(self.correoUsuario)
   
class Meta:
    verbose_name_plural = 'usuario'

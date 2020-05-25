from django.db import models
from persona.models import Persona
# Create your models here.

class Usuario(models.Model):
    Persona=models.ForeignKey(Persona, on_delete=models.CASCADE)
    correoUsario = models.CharField(max_length=200)
    contrasenaUsuario = models.CharField(max_length=200)
    def __str__(self):
        return '{}'.format(self.correoUsario)
    def save(self):
        self.Persona = self.Persona
        self.correoUsario=self.correoUsario
        self.contrasenaUsuario= self.contrasenaUsuario
        super(Usuario,self).save()

class Meta:
      verbose_name_plural='Usuario'

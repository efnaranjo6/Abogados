from django.db import models

from rol.models import Rol
from usuario.models import usuario
# Create your models here.

class Detalleusuario(models.Model):
    Rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.Rol)
    def save(self):
        
        self.Rol=self.Rol
        self.usuario = self.usuario
        super(Detalleusuario,self).save()

class Meta:
      verbose_name_plural='Detalleusuarios'

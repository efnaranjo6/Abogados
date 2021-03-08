from django.db import models
from usuario.models import usuario
from rol.models import Rol
# Create your models here.

class Detalleusuario(models.Model):
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    Rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    def __str__(self):
        return '{}{}'.format(self.usuario, self.Rol)
    def save(self):
        self.usuario = self.usuario
        self.Rol=self.Rol
        super(Detalleusuario,self).save()

class Meta:
      verbose_name_plural='Detalleusuarios'

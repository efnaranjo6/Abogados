

from rol.models import Rol
from usuario.models import User
from base.models import BaseModel
from django.db import models
# Create your models here.

class Detalleusuario(BaseModel):
    Rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.Rol)
    def save(self):
        
        self.Rol=self.Rol
        self.usuario = self.usuario
        super(Detalleusuario,self).save()

class Meta:
      verbose_name_plural='Detalleusuarios'

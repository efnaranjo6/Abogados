from django.db import models
from usuario.models import Usuario
from rol.models import Rol
# Create your models here.

class Detalleusuario(models.Model):
    Usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Rol=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    from usuario.models import Usuario
      def __str__(self):
        return '{}'.format(self.Usuario)
    def save(self):
        self.Usuario=self.Usuario
        self.Rol=self.Rol
        super(Detalleusuario,self).save()

class Meta:
      verbose_name_plural='Detalleusuarios'

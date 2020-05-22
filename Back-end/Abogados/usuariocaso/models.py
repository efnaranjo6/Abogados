from django.db import models
from caso.models import Caso
from usuario.models import Usuario

# Create your models here.


class Usuariocaso(models.Model):
    Caso = models.ForeignKey(Caso, on_delete=models.CASCADE)
    Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    

    def __str__(self):
        return '{}'.format(self.Usuario)

    def save(self):
        self.Usuario = self.Usuario
        self.Caso = self.Caso
  
        super(Usuariocaso, self).save()


class Meta:
    verbose_name_plural = 'Usuariocasos'

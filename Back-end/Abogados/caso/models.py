from django.db import models
from usuario.models import Usuario
from tipocaso.models import Tipocaso

# Create your models here.


class Caso(models.Model):
    Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Tipocaso = models.ForeignKey(Tipocaso, on_delete=models.CASCADE)
    Estado = models.CharField(max_length=200)


    def __str__(self):
        return '{}'.format(self.Usuario)

    def save(self):
        self.Usuario = self.Usuario
        self.Estado = self.Estado
        self.Tipocaso = self.Tipocaso
        super(Caso, self).save()


class Meta:
    verbose_name_plural = 'Casos'

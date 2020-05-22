from django.db import models
from caso.models import Caso

# Create your models here.


class Detallecaso(models.Model):
    
    descripccion = models.CharField(max_length=200)
    porcentaje = models.CharField(max_length=200)
    Caso = models.ForeignKey(Caso, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.Usuario)

    def save(self):
        self.Caso = self.Caso
        self.descripccion = self.descripccion
        self.porcentaje = self.porcentaje
        super(Detallecaso, self).save()


class Meta:
    verbose_name_plural = 'Casos'

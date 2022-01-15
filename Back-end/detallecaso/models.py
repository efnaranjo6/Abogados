from django.db import models
from caso.models import Caso

from base.models import BaseModel

# Create your models here.


class Detallecaso(BaseModel):
    descripccion = models.CharField(max_length=200)
    porcentaje = models.CharField(max_length=200)

    Caso = models.ForeignKey(Caso, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.usuario)
class Meta:
    verbose_name_plural = 'Casos'

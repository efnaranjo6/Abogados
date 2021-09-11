from django.db import models
from base.models import BaseModel
# Create your models here.
class Tipocaso(BaseModel):  
    nombre = models.CharField(max_length=200)
    def __str__(self):
        return '{}'.format(self.nombre)
class Meta:
    verbose_name_plural = 'Tipocasos'

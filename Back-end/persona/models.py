from django.db import models
 
from base.models import BaseModel
# Create your models here.
class Persona(BaseModel):
    nombrePersona = models.CharField(max_length=200)
    apellidoPersona = models.CharField(max_length=200)
    cedulaPersona = models.CharField(max_length=200)
    def __str__(self):
        return '{}'.format(self.nombrePersona)
  
class Meta:
      verbose_name_plural='Persona'

from django.db import models
from tipocaso.models import Tipocaso
from persona.models import Persona
from base.models import BaseModel
# Create your models here.
class Caso(BaseModel):
    Persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    Tipocaso = models.ForeignKey(Tipocaso, on_delete=models.CASCADE)
    Estado = models.CharField(max_length=200)
    def __str__(self):
        return '{}-{}-{}'.format(self.id,self.Tipocaso, self.Persona)
class Meta:
    verbose_name_plural = 'Casos'

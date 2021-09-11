
from caso.models import Caso
from base.models import BaseModel
from persona.models import Persona
from django.db import models
# Create your models here.
class Usuariocaso(BaseModel):
    Caso = models.ForeignKey(Caso, on_delete=models.CASCADE)
    Persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.Persona)
    def save(self):
        self.Persona = self.Persona
        self.Caso = self.Caso
        super(Usuariocaso, self).save()
class Meta:
    verbose_name_plural = 'Usuariocasos'

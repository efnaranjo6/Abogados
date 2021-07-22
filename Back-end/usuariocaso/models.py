from django.db import models
from caso.models import Caso
from persona.models import Persona
# Create your models here.
class Usuariocaso(models.Model):
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

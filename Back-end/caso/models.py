from django.db import models

from tipocaso.models import Tipocaso
from persona.models import Persona
# Create your models here.


class Caso(models.Model):
    Persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    Tipocaso = models.ForeignKey(Tipocaso, on_delete=models.CASCADE)
    Estado = models.CharField(max_length=200)


    def __str__(self):
        return '{}-{}-{}'.format(self.id,self.Tipocaso, self.Persona)

    def save(self):
        self.Persona = self.Persona
        self.Estado = self.Estado
        self.Tipocaso = self.Tipocaso
        super(Caso, self).save()


class Meta:
    verbose_name_plural = 'Casos'

from django.db import models


# Create your models here.


class Tipocaso(models.Model):
    
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.nombre)

    def save(self):
        self.nombre = self.nombre

        super(Tipocaso, self).save()


class Meta:
    verbose_name_plural = 'Tipo casos'

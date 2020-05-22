from django.db import models

# Create your models here.
class Rol(models.Model):

  def __str__(self):
    nombre = models.CharField(max_length=200)
    return '{}'.format(self.nombre)
  def save(self):
      self.nombre=self.nombre
      super(Rol,self).save()

class Meta:
      verbose_name_plural='Rol'

from django.db import models
# Create your models here.
class Rol(models.Model):
  nombreRol = models.CharField(max_length=200)
  def __str__(self):
      return '{}'.format(self.nombreRol)
  def save(self):
      self.nombreRol=self.nombreRol
      super(Rol,self).save()

class Meta:
      verbose_name_plural='Roles'

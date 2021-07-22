from django.db import models
from persona.models import Persona
from django.contrib.auth.models import User
# Create your models here.
class usuario(models.Model):
    correoUsuario = models.CharField(max_length=200)
    contrasenaUsuario = models.CharField(max_length=200)
    Persona = models.OneToOneField(Persona, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.correoUsuario)
    def save(self):
      self.correoUsuario = self.correoUsuario
      self.contrasenaUsuario = self.contrasenaUsuario
      self.Persona = self.Persona
      user = User.objects.create_user(
          self.correoUsuario, self.correoUsuario, self.contrasenaUsuario)
      super(usuario, self).save()
class Meta:
    verbose_name_plural = 'usuario'

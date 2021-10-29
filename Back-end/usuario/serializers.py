
from persona.serializers import PersonaSeriales
from rest_framework import serializers
from .models import User


class UsuarioS(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

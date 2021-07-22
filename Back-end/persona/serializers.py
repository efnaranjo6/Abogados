
from rest_framework import serializers
from .models import Persona
class PersonaSeriales(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

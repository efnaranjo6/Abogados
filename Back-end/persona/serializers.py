
from django.views.generic.edit import UpdateView
from rest_framework import serializers
from .models import Persona
class PersonaSeriales(serializers.ModelSerializer):

    class Meta:
        model = Persona
        fields = '__all__'
    
    def create(self,validated_data):
        persona = Persona(**validated_data)
        persona.save()
        return persona

    def update(self,instance,validated_data):
        persona_update = super().update(instance, validated_data)     
        persona_update.save()
        return persona_update

class PersonaSerialesList(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'
        
    

    
  
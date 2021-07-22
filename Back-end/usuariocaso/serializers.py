
from rest_framework import serializers
from .models import Usuariocaso


class UsuariocasoS(serializers.ModelSerializer):
    class Meta:
        model = Usuariocaso
        fields = '__all__'

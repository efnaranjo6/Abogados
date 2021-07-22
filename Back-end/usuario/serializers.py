
from rest_framework import serializers
from .models import usuario


class UsuarioS(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields = '__all__'

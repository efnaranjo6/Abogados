
from rest_framework import serializers
from .models import Caso
class CasoS(serializers.ModelSerializer):
    class Meta:
        model = Caso
        fields = '__all__'


from rest_framework import serializers
from .models import Detallecaso
class DetallecasoS(serializers.ModelSerializer):
    class Meta:
        model = Detallecaso
        fields = '__all__'

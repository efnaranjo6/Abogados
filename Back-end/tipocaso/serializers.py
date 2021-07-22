
from rest_framework import serializers
from .models import Tipocaso
class TipocasoS(serializers.ModelSerializer):
    class Meta:
        model = Tipocaso
        fields = '__all__'

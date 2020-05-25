
from rest_framework import serializers
from .models import Detalleusuario
class DetalleusuarioS(serializers.ModelSerializer):
    class Meta:
        model = Detalleusuario
        fields = '__all__'

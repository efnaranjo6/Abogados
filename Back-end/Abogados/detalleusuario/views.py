from django.shortcuts import render

from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import DetalleusuarioS
from .models import Detalleusuario


class DetalleusuarioSList(APIView):
    def get(self, request):
        detallesu = Detalleusuario.objects.all()
        data = DetalleusuarioS(detallesu, many=True).data
        return Response(data)



# Create your views here.

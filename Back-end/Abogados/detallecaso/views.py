from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import DetallecasoS
from .models import Detallecaso


class DetallecasoSList(APIView):
    def get(self, request):
        detallecaso = Detallecaso.objects.all()
        data = DetallecasoS(detallecaso, many=True).data
        return Response(data)

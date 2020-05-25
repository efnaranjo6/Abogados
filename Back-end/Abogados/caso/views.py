from django.shortcuts import render
# Create your views here.
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CasoS
from .models import Caso


class CasoSList(APIView):
    def get(self, request):
        casos = Caso.objects.all()
        data = CasoS(casos, many=True).data
        return Response(data)

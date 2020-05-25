from django.shortcuts import render
# Create your views here.
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TipocasoS
from .models import Tipocaso
class TipocasoList(APIView):
    def get(self, request):
        tiposcaso = Tipocaso.objects.all()
        data = TipocasoS(tiposcaso, many=True).data
        return Response(data)

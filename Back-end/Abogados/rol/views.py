from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RolS
from .models import Rol


class RolSList(APIView):
    def get(self, request):
        rols = Rol.objects.all()
        data = RolS(rols, many=True).data
        return Response(data)

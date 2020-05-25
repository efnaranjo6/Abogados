from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UsuarioS
from .models import Usuario


class UsuarioSList(APIView):
    def get(self, request):
        Usuarios = Usuario.objects.all()
        data = UsuarioS(Usuarios, many=True).data
        return Response(data)

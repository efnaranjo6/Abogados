from django.shortcuts import render


from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UsuariocasoS
from .models import Usuariocaso


class UsuariocasoSList(APIView):
    def get(self, request):
        usuario = Usuariocaso.objects.all()
        data = UsuariocasoS(usuario, many=True).data
        return Response(data)

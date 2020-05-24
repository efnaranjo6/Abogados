from django.shortcuts import render

from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from persona.serializers import PersonaSeriales
from persona.models import Persona


class PersonaSList(APIView):
    def get(self,request):
        personas = Persona.objects.all()
        data = PersonaSeriales(personas, many=True).data
        return Response(data)
      




# Create your views here.

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render
from .forms import personaform


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
class Personaview(generic.ListView):
    model = Persona
    template_name = 'listp.html'
    context_object_name = 'per'
class Personainsertar(generic.CreateView):
    model = Persona
    context_object_name = 'per'
    template_name = 'formp.html'
    form_class = personaform
    success_url = reverse_lazy("Persona:personas")
class Personaeditar(generic.UpdateView):
    model = Persona
    context_object_name = 'per'
    template_name = 'formp.html'
    form_class = personaform
    success_url = reverse_lazy("Persona:personas")
class Personaeliminar(generic.DeleteView):
    model = Persona
    context_object_name = 'per'
    template_name = 'deletep.html'
    form_class = personaform
    success_url = reverse_lazy("Persona:personas")


class Personalistload(generic.ListView):
    model = Persona
    template_name = 'loadp.html'
    context_object_name = 'per'
# Create your views here.

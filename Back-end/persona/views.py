from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render
from .forms import personaform
from django.contrib.auth.mixins import LoginRequiredMixin

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
class Personaview(LoginRequiredMixin,generic.ListView):
    model = Persona
    template_name = 'listp.html'
    context_object_name = 'per'
    login_url="inicio:login"
class Personainsertar(LoginRequiredMixin,generic.CreateView):
    model = Persona
    context_object_name = 'per'
    template_name = 'formp.html'
    form_class = personaform
    success_url = reverse_lazy("Persona:personas")
    login_url="inicio:login"
class Personaeditar(LoginRequiredMixin,generic.UpdateView):
    model = Persona
    context_object_name = 'per'
    template_name = 'formp.html'
    form_class = personaform
    success_url = reverse_lazy("Persona:personas")
    login_url="inicio:login"
class Personaeliminar(LoginRequiredMixin,generic.DeleteView):
    model = Persona
    context_object_name = 'per'
    template_name = 'deletep.html'
    form_class = personaform
    success_url = reverse_lazy("Persona:personas")
    login_url="inicio:login"


class Personalistload(LoginRequiredMixin,generic.ListView):
    model = Persona
    template_name = 'loadp.html'
    context_object_name = 'per'
    login_url="inicio:login"
# Create your views here.

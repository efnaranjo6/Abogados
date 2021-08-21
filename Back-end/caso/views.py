import requests
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render
from .forms import casoform
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CasoS
from .models import Caso
from detallecaso.models import Detallecaso


class CasoSList(APIView):
    def get(self, request):
        casos = Caso.objects.all()
        data = CasoS(casos, many=True).data
        return Response(data)


class Casoview(LoginRequiredMixin,generic.ListView):
    model = Caso
    template_name = 'listc.html'
    context_object_name = 'caso'
    login_url="inicio:login"
class Casoinsertar(LoginRequiredMixin,generic.CreateView):
    model = Caso
    context_object_name = 'caso'
    template_name = 'formc.html'
    form_class = casoform
    success_url = reverse_lazy("Caso:casos")
    login_url="inicio:login"      

class Casoeditar(LoginRequiredMixin,generic.UpdateView):
    model = Caso
    context_object_name = 'caso'
    template_name = 'formc.html'
    form_class = casoform
    success_url = reverse_lazy("Caso:casos")
    login_url="inicio:login"      

class Casoeliminar(LoginRequiredMixin,generic.DeleteView):
    model = Caso
    context_object_name = 'caso'
    template_name = 'deletec.html'
    form_class = casoform
    success_url = reverse_lazy("Caso:casos")
    login_url="inicio:login"

# Cr login_url="inicio:login"eate your views here.


class Casolistload(LoginRequiredMixin,generic.ListView):
    model = Caso
    template_name = 'loadc.html'
    context_object_name = 'caso'
    login_url="inicio:login"

class Casosearch(LoginRequiredMixin,generic.ListView):
    model = Detallecaso
    template_name = 'listdt.html'
    context_object_name = 'Detallecaso'
    login_url="inicio:login"
    def get_queryset(self):
        query = self.request.GET.get('name')
        print(query)
        return Detallecaso.objects.filter(Caso_id=query).order_by('id')

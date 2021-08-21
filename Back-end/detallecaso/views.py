from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render
from .forms import detallecasoform
from django.contrib.auth.mixins import LoginRequiredMixin

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


class Detallecasoview(LoginRequiredMixin,generic.ListView):
    model = Detallecaso
    template_name = 'listdc.html'
    queryset = Detallecaso.objects.all()
    context_object_name = 'dc'
    login_url="inicio:login"


class Detallecasoinsertar(LoginRequiredMixin,generic.CreateView):
    model = Detallecaso
    context_object_name = 'dc'
    template_name = 'formdc.html'
    form_class = detallecasoform
    success_url = reverse_lazy("Caso:casos")
    login_url="inicio:login"

class Detallecasoeditar(LoginRequiredMixin,generic.UpdateView):
    model = Detallecaso
    context_object_name = 'dc'
    template_name = 'formdc.html'
    form_class = detallecasoform
    success_url = reverse_lazy("Caso:casos")
    login_url="inicio:login"

class Detallecasoeliminar(LoginRequiredMixin,generic.DeleteView):
    model = Detallecaso
    context_object_name = 'dc'
    template_name = 'deletedc.html'
    form_class = detallecasoform
    success_url = reverse_lazy("Caso:casos")
    login_url="inicio:login"
# Create your views here.


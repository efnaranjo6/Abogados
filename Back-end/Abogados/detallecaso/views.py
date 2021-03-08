from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render
from .forms import detallecasoform


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


class Detallecasoview(generic.ListView):
    model = Detallecaso
    template_name = 'listdc.html'
    context_object_name = 'dc'


class Detallecasoinsertar(generic.CreateView):
    model = Detallecaso
    context_object_name = 'dc'
    template_name = 'formdc.html'
    form_class = detallecasoform
    success_url = reverse_lazy("Caso:casos")


class Detallecasoeditar(generic.UpdateView):
    model = Detallecaso
    context_object_name = 'dc'
    template_name = 'formdc.html'
    form_class = detallecasoform
    success_url = reverse_lazy("Caso:casos")


class Detallecasoeliminar(generic.DeleteView):
    model = Detallecaso
    context_object_name = 'dc'
    template_name = 'deletedc.html'
    form_class = detallecasoform
    success_url = reverse_lazy("Caso:casos")
# Create your views here.


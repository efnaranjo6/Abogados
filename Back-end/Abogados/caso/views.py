from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render
from .forms import casoform
# Create your views here.
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CasoS
from .models import Caso


class CasoSList(APIView):
    def get(self, request):
        casos = Caso.objects.all()
        data = CasoS(casos, many=True).data
        return Response(data)


class Casoview(generic.ListView):
    model = Caso
    template_name = 'listc.html'
    context_object_name = 'caso'


class Casoinsertar(generic.CreateView):
    model = Caso
    context_object_name = 'caso'
    template_name = 'formc.html'
    form_class = casoform
    success_url = reverse_lazy("Caso:casos")


class Casoeditar(generic.UpdateView):
    model = Caso
    context_object_name = 'caso'
    template_name = 'formc.html'
    form_class = casoform
    success_url = reverse_lazy("Caso:casos")


class Casoeliminar(generic.DeleteView):
    model = Caso
    context_object_name = 'caso'
    template_name = 'deletec.html'
    form_class = casoform
    success_url = reverse_lazy("Caso:casos")
# Create your views here.


class Casolistload(generic.ListView):
    model = Caso
    template_name = 'loadc.html'
    context_object_name = 'caso'


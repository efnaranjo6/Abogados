from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render
from .forms import detalleusuarioform


from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import DetalleusuarioS
from .models import Detalleusuario

class DetalleusuarioSList(APIView):
    def get(self, request):
        detallesu = Detalleusuario.objects.all()
        data = DetalleusuarioS(detallesu, many=True).data
        return Response(data)

class Detalleusuarioview(generic.ListView):
    model = Detalleusuario
    template_name = 'listdtu.html'
    context_object_name = 'detu'
    


class Detalleusuarioinsertar(generic.CreateView):
    model = Detalleusuario
    context_object_name = 'detu'
    template_name = 'formdtu.html'
    form_class = detalleusuarioform
    success_url = reverse_lazy("Detalleusuario:Detalleusuarios")


class Detalleusuarioeditar(generic.UpdateView):
    model = Detalleusuario
    context_object_name = 'detu'
    template_name = 'formdtu.html'
    form_class = detalleusuarioform
    success_url = reverse_lazy("Detalleusuario:Detalleusuarios")

class Detalleusuarioeliminar(generic.DeleteView):
    model = Detalleusuario
    context_object_name = 'detu'
    template_name = 'deletedtu.html'
    form_class = form_class = detalleusuarioform
    success_url = reverse_lazy("Detalleusuario:Detalleusuarios")
# Create your views here.



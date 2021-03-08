from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render
from .forms import rolform
# Create your views here.
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RolS
from .models import Rol


class RolSList(APIView):
    def get(self, request):
        rols = Rol.objects.all()
        data = RolS(rols, many=True).data
        return Response(data)  


class Rolview(generic.ListView):
    model = Rol
    template_name = 'listr.html'
    context_object_name = 'rol'


class Rolinsertar(generic.CreateView):
    model = Rol
    context_object_name = 'rol'
    template_name = 'formr.html'
    form_class = rolform
    success_url = reverse_lazy("rol:roles")


class Roleditar(generic.UpdateView):
    model = Rol
    context_object_name = 'rol'
    template_name = 'formr.html'
    form_class = rolform
    success_url = reverse_lazy("rol:roles")


class Roleliminar(generic.DeleteView):
    model = Rol
    context_object_name = 'rol'
    template_name = 'deleter.html'
    form_class = rolform
    success_url = reverse_lazy("rol:roles")
# Create your views here.

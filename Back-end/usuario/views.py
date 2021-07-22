from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render
from .forms import usuarioform


# Create your views here.
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UsuarioS
from .models import usuario


class UsuarioSList(APIView):
    def get(self, request):
        Usuarios = usuario.objects.all()
        data = UsuarioS(Usuarios, many=True).data
        return Response(data)
class Usuarioview(generic.ListView):
    model = usuario
    template_name = 'listu.html'
    context_object_name = 'usu'
class Usuarioinsertar(generic.CreateView):
    model = usuario
    context_object_name = 'usu'
    template_name = 'formu.html'
    form_class = usuarioform
    success_url = reverse_lazy("Usuario:usuarios")
class Usuarioeditar(generic.UpdateView):
    model = usuario
    context_object_name = 'usu'
    template_name = 'formu.html'
    form_class = usuarioform
    success_url = reverse_lazy("Usuario:usuarios")
class Usuarioeliminar(generic.DeleteView):
    model = usuario
    context_object_name = 'usu'
    template_name = 'deleteu.html'
    form_class = usuarioform
    success_url = reverse_lazy("Usuario:usuarios")
# Create your views here.
class Usuariolistload(generic.ListView):
    model = usuario
    template_name = 'loadu.html'
    context_object_name = 'usu'

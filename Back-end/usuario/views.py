from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, response
from django.shortcuts import render
from .forms import usuarioform


# Create your views here.
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UsuarioS
from .models import usuario


@api_view(['GET','POST'])
def usuario_api_view(request):

    if request.method == 'GET':
        Usuarios = usuario.objects.all()
        data = UsuarioS(Usuarios, many=True).data
        return Response(data)
    
    elif request.method == 'POST':
        Usuario = UsuarioS(data = request.data)
        if Usuario.is_valid():
            Usuario.save()
            return Response(Usuario.data)
        return Response(Usuario.errors)
     


        
       
        
    




class UsuarioSList(APIView):
    def get(self, request):
        Usuarios = usuario.objects.all()
        data = UsuarioS(Usuarios, many=True).data
        return Response(data)







class Usuarioview(LoginRequiredMixin,generic.ListView):
    model = usuario
    template_name = 'listu.html'
    context_object_name = 'usu'
    login_url="inicio:login"
class Usuarioinsertar(LoginRequiredMixin,generic.CreateView):
    model = usuario
    context_object_name = 'usu'
    template_name = 'formu.html'
    form_class = usuarioform
    success_url = reverse_lazy("Usuario:usuarios")
    login_url="inicio:login"
class Usuarioeditar(LoginRequiredMixin,generic.UpdateView):
    model = usuario
    context_object_name = 'usu'
    template_name = 'formu.html'
    form_class = usuarioform
    success_url = reverse_lazy("Usuario:usuarios")
    login_url="inicio:login"
class Usuarioeliminar(LoginRequiredMixin,generic.DeleteView):
    model = usuario
    context_object_name = 'usu'
    template_name = 'deleteu.html'
    form_class = usuarioform
    success_url = reverse_lazy("Usuario:usuarios")
    login_url="inicio:login"
# Create your views here.
class Usuariolistload(LoginRequiredMixin,generic.ListView):
    model = usuario
    template_name = 'loadu.html'
    context_object_name = 'usu'
    login_url="inicio:login"

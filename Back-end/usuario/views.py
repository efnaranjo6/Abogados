from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import usuarioform
from rest_framework import status
from rest_framework.response import Response
from .serializers import UsuarioS
from .models import usuario
from rest_framework import viewsets

class UsuarioAPIV(viewsets.ModelViewSet):
    serializer_class = UsuarioS
    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        return self.get_serializer().Meta.model.objects.filter(id=pk,state = True).first()

    def list(self,request):
        print('hola para listar Usuario')
        Usuario_serializer = self.get_serializer(self.get_queryset(),many = True)  
        return Response(Usuario_serializer.data,status = status.HTTP_200_OK)

    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Usuario registrada correctamente'},status = status.HTTP_201_CREATED )
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        self.get_queryset(pk)
        Usuario_seralizer= self.serializer_class(self.get_queryset(pk),data = request.data)
        if Usuario_seralizer.is_valid():
            Usuario_seralizer.save()
            return Response(Usuario_seralizer.data,status =status.HTTP_200_OK)
        return Response(Usuario_seralizer.errors, status = status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        Usuario= self.get_queryset().filter(id=pk).first()
        if Usuario:
            Usuario.state=False
            Usuario.save()
            return Response({"message":"Usuario Eliminado correctamente!"},status = status.HTTP_200_OK)
        return Response({"message":"no existe Usuario"},status = status.HTTP_400_BAD_REQUEST)
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

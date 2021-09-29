from django.urls import reverse_lazy
from django.views import generic
from .forms import rolform
from django.contrib.auth.mixins import LoginRequiredMixin
from .serializers import RolS
from .models import Rol
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets

class RolAPIV(viewsets.ModelViewSet):
    serializer_class = RolS
    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        return self.get_serializer().Meta.model.objects.filter(id=pk,state = True).first()

    def list(self,request):
        print('hola para listar Rol')
        Rol_serializer = self.get_serializer(self.get_queryset(),many = True)  
        return Response(Rol_serializer.data,status = status.HTTP_200_OK)

    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Rol registrada correctamente'},status = status.HTTP_201_CREATED )
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        self.get_queryset(pk)
        Rol_seralizer= self.serializer_class(self.get_queryset(pk),data = request.data)
        if Rol_seralizer.is_valid():
            Rol_seralizer.save()
            return Response(Rol_seralizer.data,status =status.HTTP_200_OK)
        return Response(Rol_seralizer.errors, status = status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        Rol= self.get_queryset().filter(id=pk).first()
        if Rol:
            Rol.state=False
            Rol.save()
            return Response({"message":"Rol Eliminado correctamente!"},status = status.HTTP_200_OK)
        return Response({"message":"no existe Rol"},status = status.HTTP_400_BAD_REQUEST)
class Rolview(LoginRequiredMixin,generic.ListView):
    model = Rol
    template_name = 'listr.html'
    context_object_name = 'rol'
    login_url="inicio:login"


class Rolinsertar(LoginRequiredMixin,generic.CreateView):
    model = Rol
    context_object_name = 'rol'
    template_name = 'formr.html'
    form_class = rolform
    success_url = reverse_lazy("rol:roles")
    login_url="inicio:login"


class Roleditar(LoginRequiredMixin,generic.UpdateView):
    model = Rol
    context_object_name = 'rol'
    template_name = 'formr.html'
    form_class = rolform
    success_url = reverse_lazy("rol:roles")
    login_url="inicio:login"


class Roleliminar(LoginRequiredMixin,generic.DeleteView):
    model = Rol
    context_object_name = 'rol'
    template_name = 'deleter.html'
    form_class = rolform
    success_url = reverse_lazy("rol:roles")
    login_url="inicio:login"


class Rolistload(LoginRequiredMixin,generic.ListView):
    model = Rol
    template_name = 'loadrol.html'
    context_object_name = 'rol'
    login_url="inicio:login"
# Create your views here.

from django.urls import reverse_lazy
from django.views import generic
from .forms import detalleusuarioform
from django.contrib.auth.mixins import LoginRequiredMixin
from .serializers import DetalleusuarioS
from .models import Detalleusuario
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets

class DetalleusuarioAPIV(viewsets.ModelViewSet):
    serializer_class = DetalleusuarioS
    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        return self.get_serializer().Meta.model.objects.filter(id=pk,state = True).first()

    def list(self,request):
        print('hola para listar Detalleusuario')
        Detalleusuario_serializer = self.get_serializer(self.get_queryset(),many = True)  
        return Response(Detalleusuario_serializer.data,status = status.HTTP_200_OK)

    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Detalleusuario registrada correctamente'},status = status.HTTP_201_CREATED )
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        self.get_queryset(pk)
        Detalleusuario_seralizer= self.serializer_class(self.get_queryset(pk),data = request.data)
        if Detalleusuario_seralizer.is_valid():
            Detalleusuario_seralizer.save()
            return Response(Detalleusuario_seralizer.data,status =status.HTTP_200_OK)
        return Response(Detalleusuario_seralizer.errors, status = status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        Detalleusuario= self.get_queryset().filter(id=pk).first()
        if Detalleusuario:
            Detalleusuario.state=False
            Detalleusuario.save()
            return Response({"message":"Detalleusuario Eliminado correctamente!"},status = status.HTTP_200_OK)
        return Response({"message":"no existe Detalleusuario"},status = status.HTTP_400_BAD_REQUEST)
class Detalleusuarioview(LoginRequiredMixin,generic.ListView):
    model = Detalleusuario
    template_name = 'listdtu.html'
    context_object_name = 'detu'
    login_url="inicio:login"


class Detalleusuarioinsertar(LoginRequiredMixin,generic.CreateView):
    model = Detalleusuario
    context_object_name = 'detu'
    template_name = 'formdtu.html'
    form_class = detalleusuarioform
    success_url = reverse_lazy("Detalleusuario:Detalleusuarios")
    login_url="inicio:login"


class Detalleusuarioeditar(LoginRequiredMixin,generic.UpdateView):
    model = Detalleusuario
    context_object_name = 'detu'
    template_name = 'formdtu.html'
    form_class = detalleusuarioform
    login_url="inicio:login"
    success_url = reverse_lazy("Detalleusuario:Detalleusuarios")

class Detalleusuarioeliminar(LoginRequiredMixin,generic.DeleteView):
    model = Detalleusuario
    context_object_name = 'detu'
    template_name = 'deletedtu.html'
    form_class = form_class = detalleusuarioform
    login_url="inicio:login"
    success_url = reverse_lazy("Detalleusuario:Detalleusuarios")
# Create your views here.



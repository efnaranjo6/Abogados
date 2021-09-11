from django.urls import reverse_lazy
from django.views import generic
from .forms import detalleusuarioform
from django.contrib.auth.mixins import LoginRequiredMixin
from .serializers import DetalleusuarioS
from .models import Detalleusuario
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics

class DetalleusuarioAPI(generics.ListAPIView):
    serializer_class = DetalleusuarioS
    def get_queryset(self):
        return  Detalleusuario.objects.filter(state = True)
class DetalleusuarioCreateAPI(generics.CreateAPIView):
    serializer_class = DetalleusuarioS
    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Usuario registrados correctamente'},status = status.HTTP_201_CREATED )
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
class DetalleusuarioRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = DetalleusuarioS
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)
class DetalleusuarioUpdateAPIView(generics. UpdateAPIView):
    serializer_class = DetalleusuarioS
    def get_queryset(self,pk):
        return self.get_serializer().Meta.model.objects.filter(state = True).filter(id=pk).first()
    def patch(self,request,pk=None):
        if self.get_queryset(pk):
            Detalleusuario_serializer=self.serializer_class(self.get_queryset(pk))
            return Response(Detalleusuario_serializer.data,status = status.HTTP_200_OK) 
        return Response({"message":"no existe Detalleusuario"},status = status.HTTP_400_BAD_REQUEST)   
    def put(self,request,pk=None):
        if self.get_queryset(pk):
            Detalleusuario_serializer=self.serializer_class(self.get_queryset(pk),data = request.data)
            if Detalleusuario_serializer.is_valid():
                Detalleusuario_serializer.save()
                return Response(Detalleusuario_serializer.data,status = status.HTTP_200_OK) 
            return Response(Detalleusuario_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
class DetalleusuarioDestroyAPIView(generics.DestroyAPIView):
    serializer_class = DetalleusuarioS
    def get_queryset(self):
        return self.get_serializer( ).Meta.model.objects.filter(state = True)
    def delete(self,request,pk=None):
        Detalleusuario= self.get_queryset().filter(id=pk).first()
        if Detalleusuario:
            Detalleusuario.state=False
            Detalleusuario.save()
            return Response({"message":"Usuario Eliminado correctamente!"},status = status.HTTP_200_OK)
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



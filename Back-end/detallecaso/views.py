
from django.urls import reverse_lazy
from django.views import generic
from .forms import detallecasoform
from django.contrib.auth.mixins import LoginRequiredMixin
from .serializers import DetallecasoS
from .models import Detallecaso
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets

class DetallecasoAPIV(viewsets.ModelViewSet):
    serializer_class = DetallecasoS
    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        return self.get_serializer().Meta.model.objects.filter(id=pk,state = True).first()

    def list(self,request):
        print('hola para listar Detallecaso')
        Detallecaso_serializer = self.get_serializer(self.get_queryset(),many = True)  
        return Response(Detallecaso_serializer.data,status = status.HTTP_200_OK)

    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Detallecaso registrada correctamente'},status = status.HTTP_201_CREATED )
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        self.get_queryset(pk)
        Detallecaso_seralizer= self.serializer_class(self.get_queryset(pk),data = request.data)
        if Detallecaso_seralizer.is_valid():
            Detallecaso_seralizer.save()
            return Response(Detallecaso_seralizer.data,status =status.HTTP_200_OK)
        return Response(Detallecaso_seralizer.errors, status = status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        Detallecaso= self.get_queryset().filter(id=pk).first()
        if Detallecaso:
            Detallecaso.state=False
            Detallecaso.save()
            return Response({"message":"Detallecaso Eliminado correctamente!"},status = status.HTTP_200_OK)
        return Response({"message":"no existe Detallecaso"},status = status.HTTP_400_BAD_REQUEST)

class Detallecasoview(LoginRequiredMixin,generic.ListView):
    model = Detallecaso
    template_name = 'listdc.html'
    queryset = Detallecaso.objects.all()
    context_object_name = 'dc'
    login_url="inicio:login"


class Detallecasoinsertar(LoginRequiredMixin,generic.CreateView):
    model = Detallecaso
    context_object_name = 'dc'
    template_name = 'formdc.html'
    form_class = detallecasoform
    success_url = reverse_lazy("Caso:casos")
    login_url="inicio:login"

class Detallecasoeditar(LoginRequiredMixin,generic.UpdateView):
    model = Detallecaso
    context_object_name = 'dc'
    template_name = 'formdc.html'
    form_class = detallecasoform
    success_url = reverse_lazy("Caso:casos")
    login_url="inicio:login"

class Detallecasoeliminar(LoginRequiredMixin,generic.DeleteView):
    model = Detallecaso
    context_object_name = 'dc'
    template_name = 'deletedc.html'
    form_class = detallecasoform
    success_url = reverse_lazy("Caso:casos")
    login_url="inicio:login"
# Create your views here.


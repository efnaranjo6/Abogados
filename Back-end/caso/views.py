import requests
from django.urls import reverse_lazy
from django.views import generic
from .forms import casoform
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from .serializers import CasoS
from .models import Caso
from detallecaso.models import Detallecaso
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets

class CasoAPIV(viewsets.ModelViewSet):
    serializer_class = CasoS
    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        return self.get_serializer().Meta.model.objects.filter(id=pk,state = True).first()

    def list(self,request):
        print('hola para listar Caso')
        Caso_serializer = self.get_serializer(self.get_queryset(),many = True)  
        return Response(Caso_serializer.data,status = status.HTTP_200_OK)

    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Caso registrado correctamente'},status = status.HTTP_201_CREATED )
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        self.get_queryset(pk)
        Caso_seralizer= self.serializer_class(self.get_queryset(pk),data = request.data)
        if Caso_seralizer.is_valid():
            Caso_seralizer.save()
            return Response(Caso_seralizer.data,status =status.HTTP_200_OK)
        return Response(Caso_seralizer.errors, status = status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        Caso= self.get_queryset().filter(id=pk).first()
        if Caso:
            Caso.state=False
            Caso.save()
            return Response({"message":"Caso Eliminado correctamente!"},status = status.HTTP_200_OK)
        return Response({"message":"no existe Caso"},status = status.HTTP_400_BAD_REQUEST)
class Casoview(LoginRequiredMixin,generic.ListView):
    model = Caso
    template_name = 'listc.html'
    context_object_name = 'caso'
    login_url="inicio:login"
class Casoinsertar(LoginRequiredMixin,generic.CreateView):
    model = Caso
    context_object_name = 'caso'
    template_name = 'formc.html'
    form_class = casoform
    success_url = reverse_lazy("Caso:casos")
    login_url="inicio:login"      

class Casoeditar(LoginRequiredMixin,generic.UpdateView):
    model = Caso
    context_object_name = 'caso'
    template_name = 'formc.html'
    form_class = casoform
    success_url = reverse_lazy("Caso:casos")
    login_url="inicio:login"      

class Casoeliminar(LoginRequiredMixin,generic.DeleteView):
    model = Caso
    context_object_name = 'caso'
    template_name = 'deletec.html'
    form_class = casoform
    success_url = reverse_lazy("Caso:casos")
    login_url="inicio:login"

# Cr login_url="inicio:login"eate your views here.


class Casolistload(LoginRequiredMixin,generic.ListView):
    model = Caso
    template_name = 'loadc.html'
    context_object_name = 'caso'
    login_url="inicio:login"

class Casosearch(LoginRequiredMixin,generic.ListView):
    model = Detallecaso
    template_name = 'listdt.html'
    context_object_name = 'Detallecaso'
    login_url="inicio:login"
    def get_queryset(self):
        query = self.request.GET.get('name')
        print(query)
        return Detallecaso.objects.filter(Caso_id=query).order_by('id')

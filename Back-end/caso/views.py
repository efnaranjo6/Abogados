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
from rest_framework import generics

class CasoAPI(generics.ListAPIView):
    serializer_class = CasoS
    def get_queryset(self):
        return  Caso.objects.filter(state = True)
class CasoCreateAPI(generics.CreateAPIView):
    serializer_class = CasoS
    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Usuario registrados correctamente'},status = status.HTTP_201_CREATED )
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
class CasoRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = CasoS
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)
class CasoUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CasoS
    def get_queryset(self,pk):
        return self.get_serializer().Meta.model.objects.filter(state = True).filter(id=pk).first()
    def patch(self,request,pk=None):
        if self.get_queryset(pk):
            Caso_serializer=self.serializer_class(self.get_queryset(pk))
            return Response(Caso_serializer.data,status = status.HTTP_200_OK) 
        return Response({"message":"no existe Caso"},status = status.HTTP_400_BAD_REQUEST)   
    def put(self,request,pk=None):
        if self.get_queryset(pk):
            Caso_serializer=self.serializer_class(self.get_queryset(pk),data = request.data)
            if Caso_serializer.is_valid():
                Caso_serializer.save()
                return Response(Caso_serializer.data,status = status.HTTP_200_OK) 
            return Response(Caso_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
class CasoDestroyAPIView(generics.DestroyAPIView):
    serializer_class = CasoS
    def get_queryset(self):
        return self.get_serializer( ).Meta.model.objects.filter(state = True)
    def delete(self,request,pk=None):
        Caso= self.get_queryset().filter(id=pk).first()
        if Caso:
            Caso.state=False
            Caso.save()
            return Response({"message":"Usuario Eliminado correctamente!"},status = status.HTTP_200_OK)
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

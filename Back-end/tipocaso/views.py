from django.urls import reverse_lazy
from django.views import generic
from .forms import tipocasoform
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from .serializers import TipocasoS
from .models import Tipocaso
from rest_framework import viewsets

class TipocasoAPIV(viewsets.ModelViewSet):
    serializer_class = TipocasoS
    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        return self.get_serializer().Meta.model.objects.filter(id=pk,state = True).first()

    def list(self,request):
        print('hola para listar Tipocaso')
        Tipocaso_serializer = self.get_serializer(self.get_queryset(),many = True)  
        return Response(Tipocaso_serializer.data,status = status.HTTP_200_OK)

    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Tipocaso registrada correctamente'},status = status.HTTP_201_CREATED )
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        self.get_queryset(pk)
        Tipocaso_seralizer= self.serializer_class(self.get_queryset(pk),data = request.data)
        if Tipocaso_seralizer.is_valid():
            Tipocaso_seralizer.save()
            return Response(Tipocaso_seralizer.data,status =status.HTTP_200_OK)
        return Response(Tipocaso_seralizer.errors, status = status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        Tipocaso= self.get_queryset().filter(id=pk).first()
        if Tipocaso:
            Tipocaso.state=False
            Tipocaso.save()
            return Response({"message":"Tipocaso Eliminado correctamente!"},status = status.HTTP_200_OK)
        return Response({"message":"no existe Tipocaso"},status = status.HTTP_400_BAD_REQUEST)
class Tipocasoview(LoginRequiredMixin,generic.ListView):
    model = Tipocaso
    template_name = 'listtc.html'
    context_object_name = 'tc'
    login_url="inicio:login"
class Tipocasoinsertar(LoginRequiredMixin,generic.CreateView):
    model = Tipocaso
    context_object_name = 'tc'
    template_name = 'formtc.html'
    form_class = tipocasoform
    success_url = reverse_lazy("Tipocaso:tiposcasos")
    login_url="inicio:login"
class Tipocasoeditar(LoginRequiredMixin,generic.UpdateView):
    model = Tipocaso
    context_object_name = 'tc'
    template_name = 'formtc.html'
    form_class = tipocasoform
    success_url = reverse_lazy("Tipocaso:tiposcasos")
    login_url="inicio:login"
class Tipocasoeliminar(LoginRequiredMixin,generic.DeleteView):
    model = Tipocaso
    context_object_name = 'tc'
    template_name = 'deletetc.html'
    form_class = tipocasoform
    success_url = reverse_lazy("Tipocaso:tiposcasos")
    login_url="inicio:login"
class Tipocasolistload(LoginRequiredMixin,generic.ListView):
    model = Tipocaso
    template_name = 'loadtc.html'
    context_object_name = 'tc'
    login_url="inicio:login"

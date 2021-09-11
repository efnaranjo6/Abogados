
from django.urls import reverse_lazy
from django.views import generic
from .forms import detallecasoform
from django.contrib.auth.mixins import LoginRequiredMixin
from .serializers import DetallecasoS
from .models import Detallecaso
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics

class DetallecasoSAPI(generics.ListAPIView):
    serializer_class = DetallecasoS
    def get_queryset(self):
        return  DetallecasoS.objects.filter(state = True)
class DetallecasoSCreateAPI(generics.CreateAPIView):
    serializer_class = DetallecasoS
    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'detalle registrados correctamente'},status = status.HTTP_201_CREATED )
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
class DetallecasoSRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = DetallecasoS
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)
class DetallecasoSUpdateAPIView(generics. UpdateAPIView):
    serializer_class = DetallecasoS
    def get_queryset(self,pk):
        return self.get_serializer().Meta.model.objects.filter(state = True).filter(id=pk).first()
    def patch(self,request,pk=None):
        if self.get_queryset(pk):
            DetallecasoS_serializer=self.serializer_class(self.get_queryset(pk))
            return Response(DetallecasoS_serializer.data,status = status.HTTP_200_OK) 
        return Response({"message":"no existe DetallecasoS"},status = status.HTTP_400_BAD_REQUEST)   
    def put(self,request,pk=None):
        if self.get_queryset(pk):
            DetallecasoS_serializer=self.serializer_class(self.get_queryset(pk),data = request.data)
            if DetallecasoS_serializer.is_valid():
                DetallecasoS_serializer.save()
                return Response(DetallecasoS_serializer.data,status = status.HTTP_200_OK) 
            return Response(DetallecasoS_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
class DetallecasoSDestroyAPIView(generics.DestroyAPIView):
    serializer_class = DetallecasoS
    def get_queryset(self):
        return self.get_serializer( ).Meta.model.objects.filter(state = True)
    def delete(self,request,pk=None):
        DetallecasoS= self.get_queryset().filter(id=pk).first()
        if DetallecasoS:
            DetallecasoS.state=False
            DetallecasoS.save()
            return Response({"message":"Detalle Eliminado correctamente!"},status = status.HTTP_200_OK)
        return Response({"message":"no existe Detalle"},status = status.HTTP_400_BAD_REQUEST)



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


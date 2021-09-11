from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import usuarioform
from rest_framework import status
from rest_framework.response import Response
from .serializers import UsuarioS
from .models import usuario
from rest_framework import generics

class UsuarioAPI(generics.ListAPIView):
    serializer_class = UsuarioS
    def get_queryset(self):
        return  usuario.objects.filter(state = True)
class UsuarioCreateAPI(generics.CreateAPIView):
    serializer_class = UsuarioS
    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Usuario registrados correctamente'},status = status.HTTP_201_CREATED )
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
class UsuarioRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UsuarioS
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)
class UsuarioUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UsuarioS
    def get_queryset(self,pk):
        return self.get_serializer().Meta.model.objects.filter(state = True).filter(id=pk).first()
    def patch(self,request,pk=None):
        if self.get_queryset(pk):
            persona_serializer=self.serializer_class(self.get_queryset(pk))
            return Response(persona_serializer.data,status = status.HTTP_200_OK) 
        return Response({"message":"no existe Usuario"},status = status.HTTP_400_BAD_REQUEST)   
    def put(self,request,pk=None):
        if self.get_queryset(pk):
            persona_serializer=self.serializer_class(self.get_queryset(pk),data = request.data)
            if persona_serializer.is_valid():
                persona_serializer.save()
                return Response(persona_serializer.data,status = status.HTTP_200_OK) 
            return Response(persona_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

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

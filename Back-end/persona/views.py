from django.urls import reverse_lazy
from django.views import generic
from .forms import personaform
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets
from .models import Persona
from .serializers import PersonaSerialesList

#Administracion en apiREST
class PersonaAPIV(viewsets.ModelViewSet):
    serializer_class = PersonaSerialesList
    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        return self.get_serializer().Meta.model.objects.filter(id=pk,state = True).first()

    def list(self,request):
        print('hola para listar persona')
        persona_serializer = self.get_serializer(self.get_queryset(),many = True)  
        return Response(persona_serializer.data,status = status.HTTP_200_OK)

    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Persona registrada correctamente'},status = status.HTTP_201_CREATED )
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        self.get_queryset(pk)
        persona_seralizer= self.serializer_class(self.get_queryset(pk),data = request.data)
        if persona_seralizer.is_valid():
            persona_seralizer.save()
            return Response(persona_seralizer.data,status =status.HTTP_200_OK)
        return Response(persona_seralizer.errors, status = status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        persona= self.get_queryset().filter(id=pk).first()
        if persona:
            persona.state=False
            persona.save()
            return Response({"message":"Persona Eliminado correctamente!"},status = status.HTTP_200_OK)
        return Response({"message":"no existe Persona"},status = status.HTTP_400_BAD_REQUEST)
    #Administracion por templates    
class Personaview(LoginRequiredMixin,generic.ListView):
    model = Persona
    template_name = 'listp.html'
    context_object_name = 'per'
    login_url="inicio:login"
class Personainsertar(LoginRequiredMixin,generic.CreateView):
    model = Persona
    context_object_name = 'per'
    template_name = 'formp.html'
    form_class = personaform
    success_url = reverse_lazy("Persona:personas")
    login_url="inicio:login"
class Personaeditar(LoginRequiredMixin,generic.UpdateView):
    model = Persona
    context_object_name = 'per'
    template_name = 'formp.html'
    form_class = personaform
    success_url = reverse_lazy("Persona:personas")
    login_url="inicio:login"
class Personaeliminar(LoginRequiredMixin,generic.DeleteView):
    model = Persona
    context_object_name = 'per'
    template_name = 'deletep.html'
    form_class = personaform
    success_url = reverse_lazy("Persona:personas")
    login_url="inicio:login"
class Personalistload(LoginRequiredMixin,generic.ListView):
    model = Persona
    template_name = 'loadp.html'
    context_object_name = 'per'
    login_url="inicio:login"
# Create your views here.


from django.urls import reverse_lazy
from django.views import generic
from .forms import personaform
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from .models import Meta, Persona
from .serializers import PersonaSerialesList
#Administracion en apiREST
class personaAPI(generics.ListAPIView):
    serializer_class = PersonaSerialesList
    def get_queryset(self):
        return  Persona.objects.filter(state = True)
class PersonaCreateAPI(generics.CreateAPIView):
    serializer_class = PersonaSerialesList
    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Usuario registrados correctamente'},status = status.HTTP_201_CREATED )
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
class PersonaRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = PersonaSerialesList
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)
class PersonaUpdateAPIView(generics. UpdateAPIView):
    serializer_class = PersonaSerialesList
    def get_queryset(self,pk):
        return self.get_serializer().Meta.model.objects.filter(state = True).filter(id=pk).first()
    def patch(self,request,pk=None):
        if self.get_queryset(pk):
            persona_serializer=self.serializer_class(self.get_queryset(pk))
            return Response(persona_serializer.data,status = status.HTTP_200_OK) 
        return Response({"message":"no existe persona"},status = status.HTTP_400_BAD_REQUEST)   
    def put(self,request,pk=None):
        if self.get_queryset(pk):
            persona_serializer=self.serializer_class(self.get_queryset(pk),data = request.data)
            if persona_serializer.is_valid():
                persona_serializer.save()
                return Response(persona_serializer.data,status = status.HTTP_200_OK) 
            return Response(persona_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
class PersonaDestroyAPIView(generics.DestroyAPIView):
    serializer_class = PersonaSerialesList
    def get_queryset(self):
        return self.get_serializer( ).Meta.model.objects.filter(state = True)
    def delete(self,request,pk=None):
        persona= self.get_queryset().filter(id=pk).first()
        if persona:
            persona.state=False
            persona.save()
            return Response({"message":"Usuario Eliminado correctamente!"},status = status.HTTP_200_OK)
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

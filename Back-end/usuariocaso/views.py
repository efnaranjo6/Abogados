
from rest_framework import status
from rest_framework.response import Response

from .serializers import UsuariocasoS
from .models import Usuariocaso
from rest_framework import generics

        
class UsuariocasoAPI(generics.ListAPIView):
    serializer_class = UsuariocasoS
    def get_queryset(self):
        return  Usuariocaso.objects.filter(state = True)
class UsuariocasoCreateAPI(generics.CreateAPIView):
    serializer_class = UsuariocasoS
    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Usuario registrados correctamente'},status = status.HTTP_201_CREATED )
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
class UsuariocasoRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UsuariocasoS
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)
class UsuariocasoUpdateAPIView(generics. UpdateAPIView):
    serializer_class = UsuariocasoS
    def get_queryset(self,pk):
        return self.get_serializer().Meta.model.objects.filter(state = True).filter(id=pk).first()
    def patch(self,request,pk=None):
        if self.get_queryset(pk):
            Usuariocaso_serializer=self.serializer_class(self.get_queryset(pk))
            return Response(Usuariocaso_serializer.data,status = status.HTTP_200_OK) 
        return Response({"message":"no existe Usuario"},status = status.HTTP_400_BAD_REQUEST)   
    def put(self,request,pk=None):
        if self.get_queryset(pk):
            Usuariocaso_serializer=self.serializer_class(self.get_queryset(pk),data = request.data)
            if Usuariocaso_serializer.is_valid():
                Usuariocaso_serializer.save()
                return Response(Usuariocaso_serializer.data,status = status.HTTP_200_OK) 
            return Response(Usuariocaso_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
class UsuariocasoDestroyAPIView(generics.DestroyAPIView):
    serializer_class = UsuariocasoS
    def get_queryset(self):
        return self.get_serializer( ).Meta.model.objects.filter(state = True)
    def delete(self,request,pk=None):
        Usuariocaso= self.get_queryset().filter(id=pk).first()
        if Usuariocaso:
            Usuariocaso.state=False
            Usuariocaso.save()
            return Response({"message":"Usuario Eliminado correctamente!"},status = status.HTTP_200_OK)
        return Response({"message":"no existe Usuariocaso"},status = status.HTTP_400_BAD_REQUEST)
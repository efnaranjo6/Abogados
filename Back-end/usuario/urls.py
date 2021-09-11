from .views import Usuarioinsertar, Usuarioeditar, Usuarioeliminar, Usuarioview,UsuarioAPI ,Usuariolistload,UsuarioCreateAPI,UsuarioRetrieveAPIView,UsuarioUpdateAPIView
from django.urls import include, path

urlpatterns = [
    path('Usuario/api/', UsuarioAPI.as_view(), name='usuariocreate'),
    path('Usuario/create/', UsuarioCreateAPI.as_view(), name='usuariocreate'),
    path('Usuario/retrieve/<int:pk>', UsuarioRetrieveAPIView.as_view(), name='usuarioretreieve'),
    path('Usuario/update/<int:pk>', UsuarioUpdateAPIView.as_view(), name='usuarioretreieve'),
    path('', Usuarioview.as_view(), name='usuarios'),
    path('loadusuario', Usuariolistload.as_view(), name='divloadU'),
    path('usuario/new/', Usuarioinsertar.as_view(), name='Insertar'),
    path('usuario/Editar/<int:pk>', Usuarioeditar.as_view(), name='Editar'),
    path('usuario/eliminar/<int:pk>', Usuarioeliminar.as_view(), name='Eliminar'),

]

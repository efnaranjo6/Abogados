from .views import Usuarioinsertar, Usuarioeditar, Usuarioeliminar, Usuarioview, Usuariolistload
from django.urls import include, path
from .views import UsuarioSList, usuario_api_view
urlpatterns = [
    path('Usuario/', usuario_api_view, name='apiusuario'),
    path('', Usuarioview.as_view(), name='usuarios'),
    path('loadusuario', Usuariolistload.as_view(), name='divloadU'),
    path('usuario/new/', Usuarioinsertar.as_view(), name='Insertar'),
    path('usuario/Editar/<int:pk>', Usuarioeditar.as_view(), name='Editar'),
    path('usuario/eliminar/<int:pk>', Usuarioeliminar.as_view(), name='Eliminar'),

]

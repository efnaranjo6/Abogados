from .loginv import Login
from .views import Usuarioinsertar, Usuarioeditar, Usuarioeliminar, Usuarioview,Usuariolistload
from django.urls import include, path

urlpatterns = [
    path('', Usuarioview.as_view(), name='usuarios'),
    path('loadusuario', Usuariolistload.as_view(), name='divloadU'),
    path('login', Login.as_view(), name='login'),
    path('usuario/new/', Usuarioinsertar.as_view(), name='Insertart'),
    path('usuario/Editar/<int:pk>', Usuarioeditar.as_view(), name='Editar'),
    path('usuario/eliminar/<int:pk>', Usuarioeliminar.as_view(), name='Eliminar'),

]

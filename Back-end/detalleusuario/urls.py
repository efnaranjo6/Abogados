from django.contrib import admin
from django.urls import include, path
from .views import Detalleusuarioview, Detalleusuarioinsertar, Detalleusuarioeditar, Detalleusuarioeliminar

urlpatterns = [
    path('', Detalleusuarioview.as_view(), name='Detalleusuarios'),
    path('detalleusuario/new',  Detalleusuarioinsertar.as_view(), name='Insertar'),
    path('detalleusuario/Editar/<int:pk>',  Detalleusuarioeditar.as_view(), name='Editar'),
    path('detalleusuario/eliminar/<int:pk>', Detalleusuarioeliminar.as_view(), name='Eliminar'),
]


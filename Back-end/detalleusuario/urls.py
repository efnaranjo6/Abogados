from django.contrib import admin
from django.urls import include, path
from .views import DetalleusuarioAPI,  Detalleusuarioview, Detalleusuarioinsertar, Detalleusuarioeditar, Detalleusuarioeliminar,DetalleusuarioCreateAPI,DetalleusuarioRetrieveAPIView,DetalleusuarioDestroyAPIView,DetalleusuarioUpdateAPIView

urlpatterns = [
    path('detalleusuario/detalleusuarios' ,DetalleusuarioAPI.as_view(), name='DetalleusuariocreateApi' ),
    path('detalleusuario/create' ,DetalleusuarioCreateAPI.as_view(), name='DetalleusuariocreateApi' ),
    path('detalleusuario/retrieve/<int:pk>', DetalleusuarioRetrieveAPIView.as_view(), name='Detalleusuario_view'),
    path('detalleusuario/delete/<int:pk>', DetalleusuarioDestroyAPIView.as_view(), name='Detalleusuario_destroeview'),
    path('detalleusuario/update/<int:pk>', DetalleusuarioUpdateAPIView.as_view(), name='Detalleusuario_upview'),
    path('', Detalleusuarioview.as_view(), name='Detalleusuarios'),
    path('detalleusuario/new',  Detalleusuarioinsertar.as_view(), name='Insertar'),
    path('detalleusuario/Editar/<int:pk>',  Detalleusuarioeditar.as_view(), name='Editar'),
    path('detalleusuario/eliminar/<int:pk>', Detalleusuarioeliminar.as_view(), name='Eliminar'),
]


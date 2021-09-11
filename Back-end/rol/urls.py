from django.contrib import admin
from django.urls import include, path
from .views import RolAPI, Rolview, Rolinsertar, Roleditar, Roleliminar, Rolistload,RolCreateAPI,RolRetrieveAPIView,RolDestroyAPIView,RolUpdateAPIView
urlpatterns = [
    path('rol/rol/' ,RolAPI.as_view(), name='RolcreateApi' ),
    path('rol/create' ,RolCreateAPI.as_view(), name='RolcreateApi' ),
    path('rol/retrieve/<int:pk>', RolRetrieveAPIView.as_view(), name='Rol_view'),
    path('rol/delete/<int:pk>', RolDestroyAPIView.as_view(), name='Rol_destroeview'),
    path('rol/update/<int:pk>', RolUpdateAPIView.as_view(), name='Rol_upview'),
    path('', Rolview.as_view(), name='roles'),
    path('loadrol', Rolistload.as_view(), name='divloadR'),
    path('rol/new', Rolinsertar.as_view(), name='Insertar'),
    path('rol/Editar/<int:pk>', Roleditar.as_view(), name='Editar'),
    path('rol/eliminar/<int:pk>', Roleliminar.as_view(), name='Eliminar'),
]

from django.contrib import admin
from django.urls import include, path
from .views import RolSList, Rolview, Rolinsertar, Roleditar, Roleliminar, Rolistload
urlpatterns = [
    path('PeRest', RolSList.as_view(), name='lr'),
    path('', Rolview.as_view(), name='roles'),
    path('loadrol', Rolistload.as_view(), name='divloadR'),
    path('rol/new', Rolinsertar.as_view(), name='Insertar'),
    path('rol/Editar/<int:pk>', Roleditar.as_view(), name='Editar'),
    path('rol/eliminar/<int:pk>', Roleliminar.as_view(), name='Eliminar'),
]

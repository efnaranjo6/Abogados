from django.contrib import admin
from django.urls import include, path
from .views import CasoSList, Casolistload, Casoview, Casoinsertar, Casoeditar, Casoeliminar
urlpatterns = [
    path('Restcaso', CasoSList.as_view(), name='cr'),
    path('', Casoview.as_view(), name='casos'),
    path('loadcaso', Casolistload.as_view(), name='divloadU'),
    path('caso/new/', Casoinsertar.as_view(), name='Insertar'),
    path('caso/Editar/<int:pk>', Casoeditar.as_view(), name='Editar'),
    path('caso/eliminar/<int:pk>', Casoeliminar.as_view(), name='Eliminar'),
]

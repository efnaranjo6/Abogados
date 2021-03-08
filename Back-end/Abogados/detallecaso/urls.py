from django.contrib import admin
from django.urls import include, path
from .views import DetallecasoSList, Detallecasoview, Detallecasoinsertar, Detallecasoeditar, Detallecasoeliminar
urlpatterns = [
    path('restdc', DetallecasoSList.as_view(), name='dr'),
    path('', Detallecasoview.as_view(), name='detallecasos'),
    path('detallecaso/new/',  Detallecasoinsertar.as_view(), name='Insertar'),
    path('detallecaso/Editar/<int:pk>',
         Detallecasoeditar.as_view(), name='Editar'),
    path('detallecaso/eliminar/<int:pk>',
         Detallecasoeliminar.as_view(), name='Eliminar'),

]

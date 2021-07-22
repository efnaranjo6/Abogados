from django.contrib import admin
from django.urls import include, path
from .views import TipocasoList, Tipocasoview, Tipocasoinsertar, Tipocasoeditar, Tipocasoeliminar, Tipocasolistload
urlpatterns = [
    path('Resttc', TipocasoList.as_view(), name='lt'),
    path('', Tipocasoview.as_view(), name='tiposcasos'),
    path('tiposcaso', Tipocasolistload.as_view(), name='divloadP'),
    path('tiposcaso/new', Tipocasoinsertar.as_view(), name='Insertar'),
    path('tiposcaso/Editar/<int:pk>', Tipocasoeditar.as_view(), name='Editar'),
    path('tiposcaso/eliminar/<int:pk>',
         Tipocasoeliminar.as_view(), name='Eliminar'),
]

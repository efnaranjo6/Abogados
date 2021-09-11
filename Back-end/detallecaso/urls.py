from django.contrib import admin
from django.urls import include, path
from .views import  Detallecasoview, Detallecasoinsertar, Detallecasoeditar, Detallecasoeliminar,DetallecasoSAPI,DetallecasoSCreateAPI,DetallecasoSRetrieveAPIView,DetallecasoSUpdateAPIView,DetallecasoSDestroyAPIView
urlpatterns = [
     path('detallecaso/detallecaso' ,DetallecasoSAPI.as_view(), name='DetallecasoScreateApi' ),
     path('detallecaso/create' ,DetallecasoSCreateAPI.as_view(), name='DetallecasoScreateApi' ),
     path('detallecaso/retrieve/<int:pk>', DetallecasoSRetrieveAPIView.as_view(), name='DetallecasoS_view'),
     path('detallecaso/delete/<int:pk>', DetallecasoSDestroyAPIView.as_view(), name='DetallecasoS_destroeview'),
     path('detallecaso/update/<int:pk>', DetallecasoSUpdateAPIView.as_view(), name='DetallecasoS_upview'),
     path('', Detallecasoview.as_view(), name='detallecasos'),
     path('detallecaso/new/',  Detallecasoinsertar.as_view(), name='Insertar'),
     path('detallecaso/Editar/<int:pk>', Detallecasoeditar.as_view(), name='Editar'),
     path('detallecaso/eliminar/<int:pk>',Detallecasoeliminar.as_view(), name='Eliminar')
]

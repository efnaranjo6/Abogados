from django.contrib import admin
from django.urls import  path
from .views import  Casolistload, Casoview, Casoinsertar, Casoeditar, Casoeliminar, CasoAPI,Casosearch,CasoCreateAPI,CasoRetrieveAPIView,CasoDestroyAPIView,CasoUpdateAPIView
urlpatterns = [
    path('caso/create' ,CasoCreateAPI.as_view(), name='casocreateApi' ),
    path('caso/' ,CasoAPI.as_view(), name='casocreateApi' ),
    path('caso/retrieve/<int:pk>', CasoRetrieveAPIView.as_view(), name='caso_view'),
    path('caso/delete/<int:pk>', CasoDestroyAPIView.as_view(), name='caso_destroeview'),
    path('caso/update/<int:pk>', CasoUpdateAPIView.as_view(), name='caso_upview'),
    path('', Casoview.as_view(), name='casos'),
    path('loadcaso', Casolistload.as_view(), name='divloadU'),
    path('caso/new/', Casoinsertar.as_view(), name='Insertar'),
    path('caso/Editar/<int:pk>', Casoeditar.as_view(), name='Editar'),
    path('caso/eliminar/<int:pk>', Casoeliminar.as_view(), name='Eliminar'),
    path('search', Casosearch.as_view(), name='search_dt')
]


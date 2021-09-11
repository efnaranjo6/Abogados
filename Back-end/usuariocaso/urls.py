
from django.contrib import admin
from django.urls import include, path
from .views import UsuariocasoCreateAPI,UsuariocasoRetrieveAPIView,UsuariocasoDestroyAPIView,UsuariocasoUpdateAPIView,UsuariocasoAPI
urlpatterns = [
    path('usuariocasos/' ,UsuariocasoAPI.as_view(), name='Usuariocaso' ),
    path('usuariocasos/create' ,UsuariocasoCreateAPI.as_view(), name='UsuariocasocreateApi' ),
    path('usuariocaso/retrieve/<int:pk>', UsuariocasoRetrieveAPIView.as_view(), name='Usuariocaso_view'),
    path('usuariocaso/delete/<int:pk>', UsuariocasoDestroyAPIView.as_view(), name='Usuariocaso_destroeview'),
    path('usuariocaso/update/<int:pk>', UsuariocasoUpdateAPIView.as_view(), name='Usuariocaso_upview')
]

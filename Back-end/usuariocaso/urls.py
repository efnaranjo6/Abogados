
from django.contrib import admin
from django.urls import include, path
from .views import UsuariocasoSList
urlpatterns = [
    path('', UsuariocasoSList.as_view(), name='udr'),
]

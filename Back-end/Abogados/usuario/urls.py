from django.contrib import admin
from django.urls import include, path
from .views import UsuarioSList
urlpatterns = [
    path('', UsuarioSList.as_view(), name='lu'),
]

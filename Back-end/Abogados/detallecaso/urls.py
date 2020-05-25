from django.contrib import admin
from django.urls import include, path
from .views import DetallecasoSList
urlpatterns = [
    path('', DetallecasoSList.as_view(), name='dr'),
]

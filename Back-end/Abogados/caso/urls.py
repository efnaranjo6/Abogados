from django.contrib import admin
from django.urls import include, path
from .views import CasoSList
urlpatterns = [
    path('', CasoSList.as_view(), name='cr'),
]

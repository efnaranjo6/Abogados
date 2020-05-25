from django.contrib import admin
from django.urls import include, path
from .views import DetalleusuarioSList
urlpatterns = [
    path('', DetalleusuarioSList.as_view(), name='dp'),
]

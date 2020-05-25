from django.contrib import admin
from django.urls import include, path
from .views import RolSList
urlpatterns = [
    path('', RolSList.as_view(), name='lr'),
]

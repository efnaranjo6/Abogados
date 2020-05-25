from django.contrib import admin
from django.urls import include, path
from .views import TipocasoList
urlpatterns = [
    path('', TipocasoList.as_view(), name='lt'),
]

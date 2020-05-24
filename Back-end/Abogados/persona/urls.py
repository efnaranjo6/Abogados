from django.contrib import admin
from django.urls import include,path
from persona.views import PersonaSList
urlpatterns=[
    path('', PersonaSList.as_view(), name='lp'),
    ]

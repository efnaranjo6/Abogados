from django.contrib import admin
from django.urls import include,path
from persona.views import PersonaSList, Personaview, Personainsertar, Personaeditar, Personaeliminar, Personalistload
urlpatterns=[
    path('PeRest', PersonaSList.as_view(), name='lp'),
    path('', Personaview.as_view(), name='personas'),
    path('loadPersona', Personalistload.as_view(), name='divloadP'),
    path('persona/new', Personainsertar.as_view(), name='Insertar'),
    path('persona/Editar/<int:pk>', Personaeditar.as_view(), name='Editar'),
    path('persona/eliminar/<int:pk>', Personaeliminar.as_view(), name='Eliminar'),

]

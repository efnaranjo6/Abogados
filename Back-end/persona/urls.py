from django.urls import include,path
from persona.views import Personaview,Personainsertar,Personaeditar,Personaeliminar,Personalistload,PersonaCreateAPI,PersonaRetrieveAPIView,PersonaDestroyAPIView,PersonaUpdateAPIView
urlpatterns=[
    path('personas/create' ,PersonaCreateAPI.as_view(), name='personacreateApi' ),
    path('', Personaview.as_view(), name='personas'),
    path('loadPersona', Personalistload.as_view(), name='divloadP'),
    path('persona/new', Personainsertar.as_view(), name='Insertar'),
    path('persona/Editar/<int:pk>', Personaeditar.as_view(), name='Editar'),
    path('persona/eliminar/<int:pk>', Personaeliminar.as_view(), name='Eliminar'),
    path('persona/retrieve/<int:pk>', PersonaRetrieveAPIView.as_view(), name='persona_view'),
    path('persona/delete/<int:pk>', PersonaDestroyAPIView.as_view(), name='persona_destroeview'),
    path('persona/update/<int:pk>', PersonaUpdateAPIView.as_view(), name='persona_upview')
]

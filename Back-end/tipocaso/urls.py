from django.contrib import admin
from django.urls import include, path
from .views import TipocasoAPI,Tipocasoview, Tipocasoinsertar, Tipocasoeditar, Tipocasoeliminar, Tipocasolistload,TipocasoCreateAPI,TipocasoRetrieveAPIView,TipocasoUpdateAPIView,TipocasoDestroyAPIView
urlpatterns = [
    path('tiposcaso/tiposcaso/' ,TipocasoAPI.as_view(), name='tiposcasocreateApi' ),
    path('tiposcaso/create' ,TipocasoCreateAPI.as_view(), name='tiposcasocreateApi' ),
    path('tiposcaso/retrieve/<int:pk>', TipocasoRetrieveAPIView.as_view(), name='tiposcaso_view'),
    path('tiposcaso/delete/<int:pk>', TipocasoDestroyAPIView.as_view(), name='tiposcaso_destroeview'),
    path('tiposcaso/update/<int:pk>', TipocasoUpdateAPIView.as_view(), name='tiposcaso_upview'),
    path('', Tipocasoview.as_view(), name='tiposcasos'),
    path('tiposcaso', Tipocasolistload.as_view(), name='divloadP'),
    path('tiposcaso/new', Tipocasoinsertar.as_view(), name='Insertar'),
    path('tiposcaso/Editar/<int:pk>', Tipocasoeditar.as_view(), name='Editar'),
    path('tiposcaso/eliminar/<int:pk>',Tipocasoeliminar.as_view(), name='Eliminar'),
]

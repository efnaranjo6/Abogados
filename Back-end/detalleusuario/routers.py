from django import urls
from rest_framework.routers import DefaultRouter
from detalleusuario.views import DetalleusuarioAPIV
router =DefaultRouter()
router.register(r'Detalleusuario',DetalleusuarioAPIV,basename = 'Detalleusuario')
urlpatterns = router.urls


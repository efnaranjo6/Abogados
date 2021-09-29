from django import urls
from rest_framework.routers import DefaultRouter
from detallecaso.views import DetallecasoAPIV
router =DefaultRouter()
router.register(r'Detallecaso',DetallecasoAPIV,basename = 'Detallecaso')
urlpatterns = router.urls


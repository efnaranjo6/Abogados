from django import urls
from rest_framework.routers import DefaultRouter
from caso.views import CasoAPIV
router =DefaultRouter()
router.register(r'Caso',CasoAPIV,basename = 'Caso')
urlpatterns = router.urls


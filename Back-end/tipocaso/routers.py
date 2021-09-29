from django import urls
from rest_framework.routers import DefaultRouter
from tipocaso.views import TipocasoAPIV
router =DefaultRouter()
router.register(r'Tipocaso',TipocasoAPIV,basename = 'Tipocaso')
urlpatterns = router.urls
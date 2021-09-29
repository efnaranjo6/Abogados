from django import urls
from rest_framework.routers import DefaultRouter
from persona.views import PersonaAPIV
router =DefaultRouter()
router.register(r'persona',PersonaAPIV,basename = 'persona')
urlpatterns = router.urls


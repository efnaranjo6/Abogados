from django import urls
from rest_framework.routers import DefaultRouter
from rol.views import RolAPIV
router =DefaultRouter()
router.register(r'Rol',RolAPIV,basename = 'Rol')
urlpatterns = router.urls
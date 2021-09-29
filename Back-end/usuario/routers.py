from django import urls
from rest_framework.routers import DefaultRouter
from usuario.views import UsuarioAPIV
router =DefaultRouter()
router.register(r'Usuario',UsuarioAPIV,basename = 'Usuario')
urlpatterns = router.urls
"""Abogados URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('inicio.urls', 'inicio'), namespace='inicio')),
    path('Persona/', include(('persona.urls', 'Persona'), namespace='Persona')),
    path('persona/', include(('persona.routers', 'persona'), namespace='persona')),
    path('Rol/', include(('rol.urls', 'rol'), namespace='Rol')),
    path('rol/', include(('rol.routers', 'rol'), namespace='Rol')),
    path('Tiposcasos/', include(('tipocaso.urls', 'Tipocaso'), namespace='Tipocaso')),
    path('tiposcasos/', include(('tipocaso.routers', 'Tipocaso'), namespace='Tipocaso')),
    path('Usuario/', include(('usuario.urls', 'Usuario'), namespace='Usuario')),
    path('usuario/', include(('usuario.routers', 'Usuario'), namespace='Usuario')),    
    path('Detalleusuario/', include(('detalleusuario.urls','detalleusuario'), namespace='Detalleusuario')),
    path('detalleusuario/', include(('detalleusuario.routers','detalleusuario'), namespace='detalleusuario')),
    path('Detallecaso/', include(('detallecaso.urls','detallecaso'), namespace='Detallecaso')),
    path('detallecaso/', include(('detallecaso.routers','detallecaso'), namespace='detallecaso')),
    path('Caso/', include(('caso.urls', 'caso'), namespace='Caso')),
    path('caso/', include(('caso.routers', 'caso'), namespace='Caso')),
    path('Usuariocaso/', include(('usuariocaso.urls','usuariocaso'), namespace='usuariocaso')),
]

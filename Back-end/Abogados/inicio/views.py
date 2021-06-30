from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from detalleusuario.models import Detalleusuario
from rol.models import Rol


class inicio(LoginRequiredMixin, generic.TemplateView): 
    template_name = "inicio.html"
    login_url = 'inicio:login'

  
    #return Response(rols)

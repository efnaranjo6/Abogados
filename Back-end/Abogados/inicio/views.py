from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from detalleusuario.models import Detalleusuario



class inicio(LoginRequiredMixin, generic.TemplateView):
    detalleusuario = Detalleusuario.objects.all()
    template_name = "inicio.html"
    login_url = 'inicio:login'

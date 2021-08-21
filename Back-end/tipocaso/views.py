from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
from .forms import tipocasoform
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TipocasoS
from .models import Tipocaso
class TipocasoList(APIView):
    def get(self, request):
        tiposcaso = Tipocaso.objects.all()
        data = TipocasoS(tiposcaso, many=True).data
        return Response(data)
class Tipocasoview(LoginRequiredMixin,generic.ListView):
    model = Tipocaso
    template_name = 'listtc.html'
    context_object_name = 'tc'
    login_url="inicio:login"
class Tipocasoinsertar(LoginRequiredMixin,generic.CreateView):
    model = Tipocaso
    context_object_name = 'tc'
    template_name = 'formtc.html'
    form_class = tipocasoform
    success_url = reverse_lazy("Tipocaso:tiposcasos")
    login_url="inicio:login"
class Tipocasoeditar(LoginRequiredMixin,generic.UpdateView):
    model = Tipocaso
    context_object_name = 'tc'
    template_name = 'formtc.html'
    form_class = tipocasoform
    success_url = reverse_lazy("Tipocaso:tiposcasos")
    login_url="inicio:login"
class Tipocasoeliminar(LoginRequiredMixin,generic.DeleteView):
    model = Tipocaso
    context_object_name = 'tc'
    template_name = 'deletetc.html'
    form_class = tipocasoform
    success_url = reverse_lazy("Tipocaso:tiposcasos")
    login_url="inicio:login"
class Tipocasolistload(LoginRequiredMixin,generic.ListView):
    model = Tipocaso
    template_name = 'loadtc.html'
    context_object_name = 'tc'
    login_url="inicio:login"

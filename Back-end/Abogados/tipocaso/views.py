from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
from .forms import tipocasoform
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
class Tipocasoview(generic.ListView):
    model = Tipocaso
    template_name = 'listtc.html'
    context_object_name = 'tc'
class Tipocasoinsertar(generic.CreateView):
    model = Tipocaso
    context_object_name = 'tc'
    template_name = 'formtc.html'
    form_class = tipocasoform
    success_url = reverse_lazy("Tipocaso:tiposcasos")
class Tipocasoeditar(generic.UpdateView):
    model = Tipocaso
    context_object_name = 'tc'
    template_name = 'formtc.html'
    form_class = tipocasoform
    success_url = reverse_lazy("Tipocaso:tiposcasos")
class Tipocasoeliminar(generic.DeleteView):
    model = Tipocaso
    context_object_name = 'per'
    template_name = 'deletetc.html'
    form_class = tipocasoform
    success_url = reverse_lazy("Tipocaso:tiposcasos")
class Tipocasolistload(generic.ListView):
    model = Tipocaso
    template_name = 'loadtc.html'
    context_object_name = 'tc'

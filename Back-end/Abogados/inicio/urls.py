
from django.contrib import admin
from django.urls import include, path
from inicio.views import inicio
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', inicio.as_view(), name='inicio'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('Logout/', auth_views.LogoutView.as_view(template_name='Logout.html'), name='logout')
]

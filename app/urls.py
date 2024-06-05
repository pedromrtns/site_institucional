from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recursos/', views.recursos, name='recursos'),
    path('contato/', views.contato, name='contato'),
    path('sobre-nos/', views.sobre_nos, name='sobre_nos'),
    path('servicos/', views.servicos, name='servicos'),
]

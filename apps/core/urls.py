from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('sobre/', views.SobreView.as_view(), name='sobre'),
    path('servicos/', views.ServicosView.as_view(), name='servicos'),
    path('contato/', views.contato, name='contato'),
] 
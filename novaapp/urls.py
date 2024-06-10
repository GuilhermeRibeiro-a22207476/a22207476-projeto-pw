# pwsite/urls.py

from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'novaapp'

urlpatterns = [
    path('inicio/', views.inicio_view, name='inicio'),
    path('detalhes/', views.detalhes_view, name='detalhes'),
    path('informacao/', views.informacao_view, name='informacao'),
]
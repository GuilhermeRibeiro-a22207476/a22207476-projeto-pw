# noobsite/urls.py

from django.urls import path
from . import views  # importamos views para poder usar as suas funções

urlpatterns = [
    path('index/', views.index_view),
    path('index1/', views.index_frase),
    path('index2/', views.index_mentira),
    path('index3/', views.index_verdade),
]
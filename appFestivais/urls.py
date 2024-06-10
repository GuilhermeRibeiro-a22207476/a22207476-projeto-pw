from django.urls import path
from . import views

app_name = 'appFestivais'

urlpatterns = [
    path('', views.localizacao_view, name='localizacoes'),
    path('festival/<int:festival_id>/', views.festival_view, name='festival'),
    path('bandas/', views.banda_view, name='bandas'),
]

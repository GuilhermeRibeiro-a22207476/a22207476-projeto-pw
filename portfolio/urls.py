from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('projeto/<int:id>/', views.projeto_detalhes_view, name='projeto_detalhes'),
    path('novo/', views.novo_projeto_view, name='novo_projeto'),
    path('projeto/<int:id>/editar/', views.editar_projeto_view, name='editar_projeto'),
    path('projeto/<int:id>/apagar/', views.apagar_projeto_view, name='apagar_projeto'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),  # Adiciona a URL de logout
]

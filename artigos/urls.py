from django.urls import path
from . import views

app_name = 'artigos'

urlpatterns = [
    path('', views.lista_autores, name='lista_autores'),
    path('artigos/<int:artigo_id>/', views.detalhe_artigo, name='detalhe_artigo'),
    path('autores/<int:autor_id>/artigos/', views.lista_artigos, name='lista_artigos'),
    path('artigos/<int:artigo_id>/comentarios/', views.comentarios_classificacoes, name='comentarios_classificacoes'),
    path('autor/novo/', views.novo_autor_view, name='novo_autor'),
    path('autor/<int:autor_id>/editar/', views.editar_autor_view, name='editar_autor'),
    path('autor/<int:autor_id>/apagar/', views.apagar_autor_view, name='apagar_autor'),
    path('artigo/novo/', views.novo_artigo_view, name='novo_artigo'),
    path('artigo/<int:artigo_id>/editar/', views.editar_artigo_view, name='editar_artigo'),
    path('artigo/<int:artigo_id>/apagar/', views.apagar_artigo_view, name='apagar_artigo'),
    path('comentario/novo/', views.novo_comentario_view, name='novo_comentario'),
    path('comentario/<int:comentario_id>/editar/', views.editar_comentario_view, name='editar_comentario'),
    path('comentario/<int:comentario_id>/apagar/', views.apagar_comentario_view, name='apagar_comentario'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

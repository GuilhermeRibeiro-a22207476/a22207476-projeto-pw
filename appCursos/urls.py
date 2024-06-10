from django.urls import path
from . import views

app_name = 'appCursos'

urlpatterns = [
    path('', views.lista_cursos_view, name='lista_cursos'),
    path('cursos/<int:curso_id>/', views.curso_view, name='curso_detalhes'),
    path('disciplinas/<int:disciplina_id>/', views.disciplina_view, name='disciplina_detalhes'),
    path('projetos/<int:projeto_id>/', views.projeto_view, name='projeto_detalhes'),
    path('curso/novo/', views.novo_curso_view, name='novo_curso'),
    path('curso/<int:curso_id>/edita/', views.editar_curso_view, name='editar_curso'),
    path('curso/<int:curso_id>/apaga/', views.apagar_curso_view, name='apagar_curso'),
    path('disciplina/nova/', views.nova_disciplina_view, name='nova_disciplina'),
    path('disciplina/<int:disciplina_id>/edita/', views.editar_disciplina_view, name='editar_disciplina'),
    path('disciplina/<int:disciplina_id>/apaga/', views.apagar_disciplina_view, name='apagar_disciplina'),
    path('projeto/novo/', views.novo_projeto_view, name='novo_projeto'),
    path('area_cientifica/nova/', views.nova_area_cientifica_view, name='nova_area_cientifica'),
    path('area_cientifica/<int:area_cientifica_id>/edita/', views.editar_area_cientifica_view, name='editar_area_cientifica'),
    path('area_cientifica/<int:area_cientifica_id>/apaga/', views.apagar_area_cientifica_view, name='apagar_area_cientifica'),
    path('linguagem_programacao/nova/', views.nova_linguagem_programacao_view, name='nova_linguagem_programacao'),
    path('linguagem_programacao/<int:linguagem_programacao_id>/edita/', views.editar_linguagem_programacao_view, name='editar_linguagem_programacao'),
    path('linguagem_programacao/<int:linguagem_programacao_id>/apaga/', views.apagar_linguagem_programacao_view, name='apagar_linguagem_programacao'),
    path('docente/novo/', views.novo_docente_view, name='novo_docente'),
    path('docente/<int:docente_id>/edita/', views.editar_docente_view, name='editar_docente'),
    path('docente/<int:docente_id>/apaga/', views.apagar_docente_view, name='apagar_docente'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

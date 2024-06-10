from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Curso, Disciplina, Projeto, AreaCientifica, Docente, LinguagemProgramacao
from .forms import CursoForm, DisciplinaForm, ProjetoForm, AreaCientificaForm, DocenteForm, LinguagemProgramacaoForm
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def lista_cursos_view(request):
    cursos = Curso.objects.all()
    context = {'cursos': cursos}
    return render(request, "appCursos/index.html", context)

def curso_view(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    disciplinas = curso.disciplina_set.all()
    context = {'curso': curso, 'disciplinas': disciplinas}
    return render(request, "appCursos/curso.html", context)

def disciplina_view(request, disciplina_id):
    disciplina = get_object_or_404(Disciplina, id=disciplina_id)
    projeto = Projeto.objects.filter(disciplina=disciplina).first()
    context = {'disciplina': disciplina, 'projeto': projeto}
    return render(request, "appCursos/disciplina.html", context)

def projeto_view(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    context = {'projeto': projeto}
    return render(request, "appCursos/projeto.html", context)

@login_required
def novo_curso_view(request):
    form = CursoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('appCursos:lista_cursos')

    return render(request, 'appCursos/novo_curso.html', {'form': form})

@login_required
def editar_curso_view(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    form = CursoForm(request.POST or None, instance=curso)
    if form.is_valid():
        form.save()
        return redirect('appCursos:curso_detalhes', curso_id=curso.id)

    return render(request, 'appCursos/editar_curso.html', {'form': form})

@login_required
def apagar_curso_view(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    curso.delete()
    return redirect('appCursos:lista_cursos')

@login_required
def nova_disciplina_view(request):
    form = DisciplinaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('appCursos:lista_cursos')

    return render(request, 'appCursos/nova_disciplina.html', {'form': form})

@login_required
def editar_disciplina_view(request, disciplina_id):
    disciplina = get_object_or_404(Disciplina, id=disciplina_id)
    form = DisciplinaForm(request.POST or None, instance=disciplina)
    if form.is_valid():
        form.save()
        return redirect('appCursos:disciplina_detalhes', disciplina_id=disciplina.id)

    return render(request, 'appCursos/editar_disciplina.html', {'form': form})

@login_required
def apagar_disciplina_view(request, disciplina_id):
    disciplina = get_object_or_404(Disciplina, id=disciplina_id)
    disciplina.delete()
    return redirect('appCursos:lista_cursos')

@login_required
def novo_projeto_view(request):
    form = ProjetoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('appCursos:lista_cursos')

    return render(request, 'appCursos/novo_projeto.html', {'form': form})

# Adicionando views para criar, editar e apagar Área Científica, Linguagem de Programação e Docente

@login_required
def nova_area_cientifica_view(request):
    form = AreaCientificaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('appCursos:lista_cursos')

    return render(request, 'appCursos/nova_area_cientifica.html', {'form': form})

@login_required
def editar_area_cientifica_view(request, area_cientifica_id):
    area_cientifica = get_object_or_404(AreaCientifica, id=area_cientifica_id)
    form = AreaCientificaForm(request.POST or None, instance=area_cientifica)
    if form.is_valid():
        form.save()
        return redirect('appCursos:lista_cursos')

    return render(request, 'appCursos/editar_area_cientifica.html', {'form': form})

@login_required
def apagar_area_cientifica_view(request, area_cientifica_id):
    area_cientifica = get_object_or_404(AreaCientifica, id=area_cientifica_id)
    area_cientifica.delete()
    return redirect('appCursos:lista_cursos')

@login_required
def nova_linguagem_programacao_view(request):
    form = LinguagemProgramacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('appCursos:lista_cursos')

    return render(request, 'appCursos/nova_linguagem_programacao.html', {'form': form})

@login_required
def editar_linguagem_programacao_view(request, linguagem_programacao_id):
    linguagem_programacao = get_object_or_404(LinguagemProgramacao, id=linguagem_programacao_id)
    form = LinguagemProgramacaoForm(request.POST or None, instance=linguagem_programacao)
    if form.is_valid():
        form.save()
        return redirect('appCursos:lista_cursos')

    return render(request, 'appCursos/editar_linguagem_programacao.html', {'form': form})

@login_required
def apagar_linguagem_programacao_view(request, linguagem_programacao_id):
    linguagem_programacao = get_object_or_404(LinguagemProgramacao, id=linguagem_programacao_id)
    linguagem_programacao.delete()
    return redirect('appCursos:lista_cursos')

@login_required
def novo_docente_view(request):
    form = DocenteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('appCursos:lista_cursos')

    return render(request, 'appCursos/novo_docente.html', {'form': form})

@login_required
def editar_docente_view(request, docente_id):
    docente = get_object_or_404(Docente, id=docente_id)
    form = DocenteForm(request.POST or None, instance=docente)
    if form.is_valid():
        form.save()
        return redirect('appCursos:lista_cursos')

    return render(request, 'appCursos/editar_docente.html', {'form': form})

@login_required
def apagar_docente_view(request, docente_id):
    docente = get_object_or_404(Docente, id=docente_id)
    docente.delete()
    return redirect('appCursos:lista_cursos')

def registo_view(request):
    if request.method == "POST":
        User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            first_name=request.POST['nome'],
            last_name=request.POST['apelido'],
            password=request.POST['password']
        )
        return redirect(reverse('login'))

    return render(request, 'appCursos/registo.html')

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect(reverse('appCursos:lista_cursos'))
        else:
            return render(request, 'appCursos/login.html', {
                'mensagem': 'Credenciais inválidas'
            })

    return render(request, 'appCursos/login.html')

def logout_view(request):
    logout(request)
    return redirect('appCursos:lista_cursos')

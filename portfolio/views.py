from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Perfil, Projeto
from .forms import ProjetoForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


def home_view(request):
    profile = Perfil.objects.first()
    projetos = Projeto.objects.all()
    context = {
        'profile': profile,
        'projetos': projetos
    }
    return render(request, 'portfolio/home.html', context)

def projeto_detalhes_view(request, id):
    projeto = get_object_or_404(Projeto, id=id)
    context = {
        'projeto': projeto
    }
    return render(request, 'portfolio/projeto_detalhes.html', context)

@login_required
def novo_projeto_view(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('portfolio:home')
    else:
        form = ProjetoForm()
    return render(request, 'portfolio/novo_projeto.html', {'form': form})

@login_required
def editar_projeto_view(request, id):
    projeto = get_object_or_404(Projeto, id=id)
    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('portfolio:projeto_detalhes', id=projeto.id)
    else:
        form = ProjetoForm(instance=projeto)
    return render(request, 'portfolio/editar_projeto.html', {'form': form, 'projeto': projeto})

@login_required
def apagar_projeto_view(request, id):
    projeto = get_object_or_404(Projeto, id=id)
    if request.method == 'POST':
        projeto.delete()
        return redirect('portfolio:home')
    return render(request, 'portfolio/apagar_projeto.html', {'projeto': projeto})
    
def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('portfolio:home')  # Redireciona para a página inicial após login bem-sucedido
        else:
            return render(request, 'portfolio/login.html', {
                'mensagem': 'Credenciais inválidas'
            })
        
    return render(request, 'portfolio/login.html')


def logout_view(request):
    logout(request)
    return redirect('portfolio:home')  # Redireciona para a página inicial após logout

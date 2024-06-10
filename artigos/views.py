from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Autor, Artigo, Comentario
from .forms import AutorForm, ArtigoForm, ComentarioForm

def lista_autores(request):
    autores = Autor.objects.all()
    return render(request, 'artigos/lista_autores.html', {'autores': autores})

def lista_artigos(request, autor_id):
    autor = Autor.objects.get(id=autor_id)
    artigos = Artigo.objects.filter(autor=autor)
    return render(request, 'artigos/lista_artigos.html', {'autor': autor, 'artigos': artigos})

def comentarios_classificacoes(request, artigo_id):
    artigo = Artigo.objects.get(id=artigo_id)
    comentarios = Comentario.objects.filter(post=artigo)
    return render(request, 'artigos/comentarios_classificacoes.html', {'artigo': artigo, 'comentarios': comentarios})

def detalhe_artigo(request, artigo_id):
    artigo = Artigo.objects.get(id=artigo_id)
    return render(request, 'artigos/detalhe_artigo.html', {'artigo': artigo})

@login_required
def novo_autor_view(request):
    form = AutorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('artigos:lista_autores')

    return render(request, 'artigos/novo_autor.html', {'form': form})

@login_required
def editar_autor_view(request, autor_id):
    autor = Autor.objects.get(id=autor_id)
    form = AutorForm(request.POST or None, instance=autor)
    if form.is_valid():
        form.save()
        return redirect('artigos:lista_autores')

    return render(request, 'artigos/editar_autor.html', {'form': form})

@login_required
def apagar_autor_view(request, autor_id):
    autor = Autor.objects.get(id=autor_id)
    autor.delete()
    return redirect('artigos:lista_autores')

@login_required
def novo_artigo_view(request):
    form = ArtigoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('artigos:lista_autores')

    return render(request, 'artigos/novo_artigo.html', {'form': form})

@login_required
def editar_artigo_view(request, artigo_id):
    artigo = Artigo.objects.get(id=artigo_id)
    form = ArtigoForm(request.POST or None, instance=artigo)
    if form.is_valid():
        form.save()
        return redirect('artigos:lista_artigos', autor_id=artigo.autor.id)  # Certifique-se de que autor_id é passado corretamente

    return render(request, 'artigos/editar_artigo.html', {'form': form, 'artigo': artigo})

@login_required
def apagar_artigo_view(request, artigo_id):
    artigo = Artigo.objects.get(id=artigo_id)
    artigo.delete()
    return redirect('artigos:lista_autores')

@login_required
def novo_comentario_view(request):
    form = ComentarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('artigos:lista_autores')

    return render(request, 'artigos/novo_comentario.html', {'form': form})

@login_required
def editar_comentario_view(request, comentario_id):
    comentario = Comentario.objects.get(id=comentario_id)
    form = ComentarioForm(request.POST or None, instance=comentario)
    if form.is_valid():
        form.save()
        return redirect('artigos:lista_autores')

    return render(request, 'artigos/editar_comentario.html', {'form': form})

@login_required
def apagar_comentario_view(request, comentario_id):
    comentario = Comentario.objects.get(id=comentario_id)
    artigo_id = comentario.post.id
    comentario.delete()
    return redirect('artigos:comentarios_classificacoes', artigo_id=artigo_id)

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect(reverse('artigos:lista_autores'))
        else:
            return render(request, 'artigos/login.html', {
                'mensagem': 'Credenciais inválidas'
            })

    return render(request, 'artigos/login.html')

def logout_view(request):
    logout(request)
    return redirect('artigos:lista_autores')

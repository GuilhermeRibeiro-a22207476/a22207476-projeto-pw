from django.shortcuts import render, redirect
from .models import Banda, Album, Musica
from .forms import BandaForm, AlbumForm
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Página com a lista de bandas.
def listaBandas_view(request):
    bandas = Banda.objects.all()
    context = {'bandas': bandas}
    return render(request, "appBandas/bandas.html", context)

# Página de uma banda, com lista de álbuns.
def banda_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)
    albuns = banda.albuns.all()  # Corrigindo para usar o nome correto do relacionamento
    context = {'banda': banda, 'albuns': albuns}
    return render(request, "appBandas/bandaAlbuns.html", context)

# Página de um álbum, que mostra informações do álbum, incluindo a imagem da capa.
def album_view(request, album_id):
    album = Album.objects.get(id=album_id)
    musicas = album.musicas.all()  # Corrigindo para usar o nome correto do relacionamento
    context = {'album': album, 'musicas': musicas}
    return render(request, "appBandas/albumMusicas.html", context)

# Página de uma música, que mostra informações disponíveis.
def musica_view(request, musica_id):
    musica = Musica.objects.get(id=musica_id)
    context = {'musica': musica}
    return render(request, "appBandas/musicas.html", context)

#-----------------------------------------------------------------------------------------------------

@login_required
def novo_banda_view(request):
    form = BandaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('appBandas:bandas')

    context = {'form': form}
    return render(request, 'appBandas/novo_banda.html', context)

@login_required
def edita_banda_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)
    if request.POST:
        form = BandaForm(request.POST or None, request.FILES or None, instance=banda)
        if form.is_valid():
            form.save()
            return redirect('appBandas:bandas')
    else:
        form = BandaForm(instance=banda)

    context = {'form': form, 'banda': banda}
    return render(request, 'appBandas/edita_banda.html', context)

@login_required
def apaga_banda_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)
    banda.delete()
    return redirect('appBandas:bandas')

@login_required
def novo_album_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)
    form = AlbumForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        album = form.save(commit=False)
        album.banda = banda
        album.save()
        return redirect('appBandas:bandaAlbuns', banda_id=banda.id)

    context = {'form': form, 'banda': banda}
    return render(request, 'appBandas/novo_album.html', context)

def registo_view(request):
    if request.method == "POST":
        User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            first_name=request.POST['nome'],
            last_name=request.POST['apelido'],
            password=request.POST['password']
        )
        return redirect(reverse('appBandas:login'))

    return render(request, 'appBandas/registo.html')

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect(reverse('appBandas:bandas'))
        else:
            return render(request, 'appBandas/login.html', {
                'mensagem': 'Credenciais inválidas'
            })

    return render(request, 'appBandas/login.html')

def logout_view(request):
    logout(request)
    return redirect('appBandas:bandas')

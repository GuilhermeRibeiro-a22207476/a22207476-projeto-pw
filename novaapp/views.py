# pwsite/views.py

from django.shortcuts import render

def inicio_view(request):
    return render(request, "novaapp/inicio.html")

def detalhes_view(request):
    return render(request, "novaapp/detalhes.html")

def informacao_view(request):
    return render(request, "novaapp/informacao.html")
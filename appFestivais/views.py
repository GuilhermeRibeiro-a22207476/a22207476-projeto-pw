from django.shortcuts import render

from .models import Localizacao, Festival, Banda

def localizacao_view(request):
    localizacoes = Localizacao.objects.all()
    context = {'localizacoes': localizacoes}
    return render(request, "appFestivais/listaFestivais.html", context)

def listaFestivais_view(request, festival_id):
    festival = Festival.objects.get(id=festival_id)
    context = {'festival': festival}
    return render(request, "appFestivais/listaFestivais.html", context)

def banda_view(request):
    bandas = Banda.objects.all()
    context = {'bandas': bandas}
    return render(request, "appFestivais/festival.html", context)

def festival_view(request, festival_id):
    festival = Festival.objects.get(id=festival_id)
    context = {'festival': festival}
    return render(request, 'appFestivais/festival.html', context)
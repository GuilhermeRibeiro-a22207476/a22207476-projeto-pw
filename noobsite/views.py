

from django.http import HttpResponse

def index_view(request):
    return HttpResponse("Olá n00b, esta é a página web mais básica do mundo!")

def index_frase(request):
    return HttpResponse("Adoro programar")

def index_mentira(request):
    return HttpResponse("Ultima frase era uma mentira")

def index_verdade(request):
    return HttpResponse("Ultima frase era verdade")
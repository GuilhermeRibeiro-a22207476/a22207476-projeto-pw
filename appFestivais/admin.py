from django.contrib import admin

from .models import Localizacao, Festival, Banda

class LocalizacaoAdmin(admin.ModelAdmin):
    list_display = ('cidade', 'pais')
    ordering = ('cidade', 'pais')
    search_fields = ('cidade', 'pais')

admin.site.register(Localizacao, LocalizacaoAdmin)

class FestivalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'localizacao')
    ordering = ('nome', 'localizacao')
    search_fields = ('nome', 'localizacao')

admin.site.register(Festival, FestivalAdmin)

class BandaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'genero', 'nMembros', 'festival')
    ordering = ('nome', 'genero', 'festival')
    search_fields = ('nome', 'genero', 'festival')

admin.site.register(Banda, BandaAdmin)

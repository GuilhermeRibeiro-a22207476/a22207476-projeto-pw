from django.contrib import admin

from .models import Banda
from .models import Album
from .models import Musica

class BandaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nMembros')
    ordering = ('nome',)  # Note a vírgula após 'nome' para torná-lo uma tupla
    search_fields = ('nome',)  # Note a vírgula após 'nome' para torná-lo uma tupla

admin.site.register(Banda, BandaAdmin)

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('nome', 'banda', 'nMusicas', 'ano_lancamento')
    ordering = ('nome', 'banda', 'nMusicas')
    search_fields = ('nome', )

admin.site.register(Album, AlbumAdmin)

class MusicaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'album', 'ano_lancamento', 'duracao', 'spotify')
    ordering = ('nome', 'album', 'ano_lancamento', 'duracao')
    search_fields = ('nome', )  # Corrigido para referenciar o campo 'titulo' do modelo 'Album'

admin.site.register(Musica, MusicaAdmin)


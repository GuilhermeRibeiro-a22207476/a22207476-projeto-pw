from django.contrib import admin

from .models import Autor, Artigo, Comentario

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', )
    ordering = ('nome',)
    search_fields = ('nome',)
admin.site.register(Autor, AutorAdmin)

class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('title', 'autor', 'data' )
    ordering = ('title', 'autor', 'data')
    search_fields = ('nome', 'autor')
admin.site.register(Artigo, ArtigoAdmin)

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('post', 'autor', 'rating')
    ordering = ('post', 'autor', 'rating')
    search_fields = ('post', 'autor', 'rating')
admin.site.register(Comentario, ComentarioAdmin)
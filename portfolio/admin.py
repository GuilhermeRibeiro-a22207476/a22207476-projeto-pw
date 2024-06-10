from django.contrib import admin
from .models import Perfil, Projeto

class PerfilAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    ordering = ('name',)
    search_fields = ('name',)

admin.site.register(Perfil, PerfilAdmin)

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')
    ordering = ('title',)
    search_fields = ('title',)

admin.site.register(Projeto, ProjetoAdmin)

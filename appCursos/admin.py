from django.contrib import admin
from .models import Curso, AreaCientifica, Disciplina, Projeto, LinguagemProgramacao, Docente

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'apresentacao', 'competencias', 'objetivos')
    ordering = ('nome', 'apresentacao', 'competencias', 'objetivos')  # Note a vírgula após 'nome' para torná-lo uma tupla
    search_fields = ('nome',)

admin.site.register(Curso, CursoAdmin)

class AreaCientificaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    ordering = ('nome',)  # Note a vírgula após 'nome' para torná-lo uma tupla
    search_fields = ('nome',)

admin.site.register(AreaCientifica, AreaCientificaAdmin)

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano', 'semestre', 'ects', 'curricular', 'area_cientifica', 'curso')
    ordering = ('nome', 'ano', 'semestre', 'ects', 'curricular', 'area_cientifica', 'curso')  # Note a vírgula após 'nome' para torná-lo uma tupla
    search_fields = ('nome', 'ano', 'semestre', 'area_cientifica', 'curso')

admin.site.register(Disciplina, DisciplinaAdmin)

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('disciplina', 'descricao', 'conceitos_usados', 'tecnologias_usadas', 'imagem', 'video', 'github')
    ordering = ('disciplina', 'descricao', 'conceitos_usados', 'tecnologias_usadas', 'video', 'github')  # Note a vírgula após 'nome' para torná-lo uma tupla
    search_fields = ('disciplina', 'conceitos_usados', 'tecnologias_usadas')

admin.site.register(Projeto, ProjetoAdmin)

class LinguagemProgramacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'get_projetos')

    def get_projetos(self, obj):
        return ", ".join([p.nome for p in obj.projetos.all()])

    get_projetos.short_description = 'Projetos'  # Altera o cabeçalho da coluna

admin.site.register(LinguagemProgramacao, LinguagemProgramacaoAdmin)

class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'get_disciplinas')

    def get_disciplinas(self, obj):
        return ", ".join([d.nome for d in obj.disciplinas.all()])

    get_disciplinas.short_description = 'Disciplinas'  # Altera o cabeçalho da coluna

admin.site.register(Docente, DocenteAdmin)

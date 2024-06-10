from django import forms
from .models import Curso, AreaCientifica, Disciplina, Projeto, LinguagemProgramacao, Docente

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome do Curso'}),
            'apresentacao': forms.Textarea(attrs={'placeholder': 'Apresentação'}),
            'objetivos': forms.Textarea(attrs={'placeholder': 'Objetivos'}),
            'competencias': forms.Textarea(attrs={'placeholder': 'Competências'}),
        }

class AreaCientificaForm(forms.ModelForm):
    class Meta:
        model = AreaCientifica
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome da Área Científica'}),
        }

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome da Disciplina'}),
            'ano': forms.NumberInput(attrs={'placeholder': 'Ano'}),
            'semestre': forms.TextInput(attrs={'placeholder': 'Semestre'}),
            'ects': forms.NumberInput(attrs={'placeholder': 'ECTS'}),
            'curricular': forms.TextInput(attrs={'placeholder': 'Curricular'}),
            'area_cientifica': forms.Select(),
            'curso': forms.Select(),
        }

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'
        widgets = {
            'descricao': forms.Textarea(attrs={'placeholder': 'Descrição'}),
            'conceitos_usados': forms.Textarea(attrs={'placeholder': 'Conceitos Usados'}),
            'tecnologias_usadas': forms.Textarea(attrs={'placeholder': 'Tecnologias Usadas'}),
            'imagem': forms.ClearableFileInput(),
            'video': forms.URLInput(attrs={'placeholder': 'URL do Vídeo'}),
            'github': forms.URLInput(attrs={'placeholder': 'URL do GitHub'}),
        }

class LinguagemProgramacaoForm(forms.ModelForm):
    class Meta:
        model = LinguagemProgramacao
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome da Linguagem'}),
            'projetos': forms.SelectMultiple(),
        }

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome do Docente'}),
            'disciplinas': forms.SelectMultiple(),
        }

from django import forms
from .models import Autor, Artigo, Comentario

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'
        
        widgets = {
            'nome': forms.TextInput(attrs={
                'placeholder': 'Nome do Autor',
            }),
        }

class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigo
        fields = '__all__'
        
        labels = {
            'title': 'Título',
            'post': 'Conteúdo',
            'autor': 'Autor',
            'data': 'Data de Publicação',
        }
        
        help_texts = {
            'data': 'Verifique a data de publicação',
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'
        
        labels = {
            'autor': 'Nome',
            'texto': 'Comentário',
            'rating': 'Avaliação',
            'post': 'Artigo',
        }
        
        help_texts = {
            'rating': 'Escolha uma classificação',
        }

        widgets = {
            'autor': forms.TextInput(attrs={
                'placeholder': 'Seu Nome',
            }),
            'texto': forms.Textarea(attrs={
                'placeholder': 'Seu Comentário',
            }),
        }

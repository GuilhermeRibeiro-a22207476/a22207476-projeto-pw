from django import forms
from .models import Banda, Album, Musica

class BandaForm(forms.ModelForm):
    class Meta:
        model = Banda
        fields = '__all__'
        
        widgets = {
            'nome': forms.TextInput(attrs={
                'placeholder': 'Nome da Banda',
            }),
            'nMembros': forms.NumberInput(attrs={
                'placeholder': 'Número de Membros',
            }),
            'imagem': forms.ClearableFileInput(),
        }

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        
        labels = {
            'nome': 'Nome do Álbum',
            'ano_lancamento': 'Ano de Lançamento',
            'nMusicas': 'Número de Músicas',
            'capa': 'Capa do Álbum',
            'banda': 'Banda',
        }
        
        help_texts = {
            'ano_lancamento': 'Verifique o ano de lançamento', 
        }

class MusicaForm(forms.ModelForm):
    class Meta:
        model = Musica
        fields = '__all__'
        
        labels = {
            'nome': 'Nome da Música',
            'ano_lancamento': 'Ano de Lançamento',
            'album': 'Álbum',
            'spotify': 'Link no Spotify',
            'duracao': 'Duração',
        }
        
        help_texts = {
            'ano_lancamento': 'Verifique o ano de lançamento',
            'spotify': 'Insira o link completo do Spotify',
        }

        widgets = {
            'nome': forms.TextInput(attrs={
                'placeholder': 'Nome da Música',
            }),
            'duracao': forms.TextInput(attrs={
                'placeholder': 'Duração (min:seg)',
            }),
        }

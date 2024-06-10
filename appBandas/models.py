from django.db import models

class Banda(models.Model):
    nome = models.CharField(max_length=50)
    nMembros = models.IntegerField()
    imagem = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nome


class Album(models.Model):
    nome = models.CharField(max_length=100)
    ano_lancamento = models.CharField(max_length=30, default='0')
    nMusicas = models.IntegerField()
    capa = models.ImageField(null=True, blank=True)
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE, related_name='albuns')

    def __str__(self):
        return self.nome


class Musica(models.Model):
    nome = models.CharField(max_length=30)
    ano_lancamento = models.CharField(max_length=30, default='0')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='musicas')
    spotify = models.URLField(null=True, max_length=200)
    duracao = models.CharField(max_length=20, default='0')

    def __str__(self):
        return self.nome

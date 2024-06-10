from django.db import models

class Localizacao(models.Model):
    cidade = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)


class Festival(models.Model):
    nome = models.CharField(max_length=50)
    localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE, related_name='festivais')
    capa = models.ImageField(upload_to='festival_covers/', null=True, blank=True)

    def __str__(self):
        return self.nome



class Banda(models.Model):
    nome = models.CharField(max_length=50)
    nMembros = models.IntegerField()
    genero = models.CharField(max_length=50)
    festival = models.ForeignKey(Festival, on_delete=models.CASCADE, related_name='bandas')

    def __str__(self):
        return self.nome
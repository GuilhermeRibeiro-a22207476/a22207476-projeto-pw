from django.db import models
import datetime



class Autor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome}'

class Artigo(models.Model):
    title = models.CharField(max_length=100)
    post = models.TextField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, null=True)
    data = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f'{self.title}'


class Comentario(models.Model):
    autor = models.CharField(max_length=100)
    texto = models.TextField()

    MUITO_MAU = '1'
    MAU = '2'
    INDIFERENTE = '3'
    BOM = '4'
    MUITO_BOM = '5'

    RATINGS_CHOICES = [
        (MUITO_MAU, '1'),
        (MAU, '2'),
        (INDIFERENTE, '3'),
        (BOM, '4'),
        (MUITO_BOM, '5'),
    ]

    rating = models.CharField(max_length=10, choices=RATINGS_CHOICES, default=MUITO_MAU, blank=True, null=True)
    post = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='comentarios')

    def str(self):
        return self.autor
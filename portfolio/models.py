from django.db import models

class Perfil(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField()
    profile_picture = models.ImageField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return self.name

class Projeto(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

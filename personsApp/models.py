from django.db import models

class Pessoa(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=50)
    age = models.IntegerField()
    dateOfBirth = models.DateField()

    def __str__(self):
        return f'{self.firstName} {self.lastName} - {self.age} anos'
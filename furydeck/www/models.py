from django.db import models

# Create your models here.
class Card(models.Model):

    name = models.CharField(max_length=100,)
    img = models.ImageField(upload_to='static/img')
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name
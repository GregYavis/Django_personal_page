from django.db import models

# Create your models here.
#Создать модель типа Title/Description

class Portfolio_Article(models.Model):
    title = models.CharField(max_length=10000)
    text = models.TextField()

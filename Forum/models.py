from django.db import models

# Create your models here.
class Question(models.Model):
    title=models.CharField(max_length=100)
    author=models.TextField(max_length=1000)
    create_date=models.DateField()

class Answer(models.Model):
    answer=models.CharField(max_length=100)
    author=models.TextField(max_length=1000)
    create_date=models.DateField()


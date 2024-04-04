from django.db import models

# Create your models here.

class TrainingData(models.Model):
    review = models.CharField(max_length=200)
    label = models.CharField(max_length=20)

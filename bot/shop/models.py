from django.db import models
class Games(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()

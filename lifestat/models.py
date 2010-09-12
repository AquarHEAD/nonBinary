from django.db import models

# Create your models here.
class Stat(models.Model):
    content = models.TextField()
    stat_date = models.DateTimeField()
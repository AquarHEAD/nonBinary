from django.db import models
from django.forms import ModelForm

# Create your models here.
class Stat(models.Model):
    content = models.TextField()
    stat_date = models.DateTimeField()
    
class StatForm(ModelForm):
    class Meta:
        model = Stat
        exclude = ('stat_date',)
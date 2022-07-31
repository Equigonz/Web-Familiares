from datetime import datetime
from django.db import models

# Create your models here.
class Familiar(models.Model):
    name = models.CharField(max_length=40)
    parentezco = models.CharField(max_length=40)
    nacimiento = models.DateField(auto_now_add=True, null=True, blank=True)

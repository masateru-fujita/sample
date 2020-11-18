from django.db import models
from django.utils import timezone

class Users(models.Model):
    name = models.CharField(max_length=30)
    date_created = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.name
from django.db import models

# Create your models here.
class Personal(models.Model):
    name = models.CharField(max_length=255, unique=True)
    age = models.IntegerField()
    race = models.CharField(max_length=255, unique=True)
    discipline = models.CharField(max_length=255)
    hobbies = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    class meta:
        ordering = ['created']
    
    def __str__(self):
        return self.name
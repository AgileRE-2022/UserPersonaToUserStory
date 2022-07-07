from django.db import models

# Create your models here.
class UserPersona(models.Model) :
    nama = models.CharField(max_length=50)
    as_a = models.CharField(max_length=50)
    needs = models.TextField(max_length=1000)
    goals = models.TextField(max_length=1000)
    locations = models.CharField(max_length=255, null=True)
    bio = models.TextField(max_length=1000, null=True)
    frustrations = models.TextField(max_length=1000, null=True)
    behaviours = models.TextField(max_length=1000, null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return self.as_a
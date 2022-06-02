from django.db import models

# Create your models here.
class UserPersona(models.Model) :
    nama = models.CharField(max_length=50)
    as_a = models.CharField(max_length=50)
    needs = models.CharField(max_length=255)
    goals = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return self.as_a
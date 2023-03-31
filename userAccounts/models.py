from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=13)
    muncipality = models.CharField(max_length=100)
    district = models.CharField(max_length=150)
    password = models.CharField(max_length=5000)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    

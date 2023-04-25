from django.db import models
from hospitalAccounts.models import Doctor
# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=13)
    password = models.CharField(max_length=5000)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    

class Booking(models.Model):

    name = models.CharField(max_length=20)
    age = models.IntegerField()
    phone = models.CharField(max_length=10)
    token = models.CharField(max_length=20)
    date = models.DateField()
    address = models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)


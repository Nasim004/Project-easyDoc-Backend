from django.db import models

# Create your models here.


class Hospital(models.Model):

    name = models.CharField(max_length=150)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=30)
    admin_name = models.CharField(max_length=30)
    admin_position = models.CharField(max_length=30)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=50)
    muncipality = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    is_approved = models.BooleanField(default=False)


class Department(models.Model):
    name = models.CharField(max_length=100)
    hospital = models.ManyToManyField(Hospital, related_name='departments')


class Doctor(models.Model):
    name = models.CharField(max_length=20)
    experience = models.FloatField(max_length=4)
    hospital =models.ForeignKey(Hospital,on_delete=models.CASCADE)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    tokens = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)


class Notifications(models.Model):
    message = models.CharField(max_length=200)

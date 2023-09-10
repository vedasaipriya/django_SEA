from django.db import models


# Create your models here.

class RegisterStore(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=25)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)


class Employee(models.Model):
    empid = models.CharField(max_length=5)
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    designation = models.CharField(max_length=150)

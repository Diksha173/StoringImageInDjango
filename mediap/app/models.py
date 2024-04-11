from django.db import models

# Create your models here.
class Rform(models.Model):
    name=models.CharField(max_length=100)
    Phone_No=models.CharField(max_length=20)
    Email=models.EmailField(max_length=254)
    password=models.CharField(max_length=50)
    profile=models.ImageField()

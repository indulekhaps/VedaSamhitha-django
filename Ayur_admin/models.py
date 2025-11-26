from django.db import models

# Create your models here.
class Categorydb(models.Model):
    CategoryName=models.CharField(max_length=40,blank=True,null=True)
    Description=models.TextField(blank=True,null=True)
    CategoryImage=models.ImageField(upload_to="Category",null=True,blank=True)

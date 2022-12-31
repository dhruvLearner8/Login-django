from django.db import models

# Create your models here.
from django.db import models

class User_details(models.Model):
    
    email=models.EmailField(default="",blank=True,null=True,max_length=50)
    password=models.CharField(default="",blank=True,null=True,max_length=20)
    age=models.IntegerField(default=0)
    full_name=models.CharField(default="",blank=True,null=True,max_length=20)
    dob = models.DateField(auto_now=True,max_length=8)
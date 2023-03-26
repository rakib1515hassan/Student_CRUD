from django.db import models

# Create your models here.
class Student_info(models.Model):
    roll=models.CharField(max_length=10)
    full_name=models.CharField(max_length=20)
    image=models.ImageField(upload_to='profilePIC')
    department=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=13)

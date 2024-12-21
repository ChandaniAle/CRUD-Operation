from django.db import models

# Create your models here.
class Stduent(models.Model):
    name=models.CharField(max_length=100, null=True)
    age=models.IntegerField(default=0)
    email=models.EmailField(default="chadaniale123@gmail.com")
    phone_number=models.CharField(max_length=100)
    IsDelete=models.BooleanField(default=False)
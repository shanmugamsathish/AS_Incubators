from django.db import models

# Create your models here.
class user1(models.Model):
    Username= models.CharField(max_length = 50)
    firstname= models.CharField(max_length = 50,blank=True)
    lastname= models.CharField(max_length = 50,blank=True)
    Email= models.CharField(max_length = 50)
    Mobile = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    





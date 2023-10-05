from django.db import models

# Create your models here.

class Product(models.Model):
    
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField(blank=True,default="10000")
    offer = models.BooleanField(default=False)

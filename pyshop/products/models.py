from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200,null=True)
    description = models.TextField(null=True)
    originalPrice = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    badge = models.CharField(max_length=50, blank=True, null=True)
    unit = models.CharField(max_length=50, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    stock = models.IntegerField()
    imageUrl = models.CharField(max_length=200)

class offer(models.Model):
    description = models.CharField(max_length=200)
    discount = models.FloatField()
    code = models.CharField(max_length=10)

def __str__(self):
    return self.name
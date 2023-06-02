from django.db import models

# Vendor model

class Vendor(models.Model):
    full_name=models.CharField(max_length=50)
    photo=models.ImageField(upload_to='vendor/')
    address=models.TextField()
    mobile=models.CharField(max_length=15)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.full_name

# Unit model
class Unit(models.Model):
    title=models.CharField(max_length=50)
    short_name=models.CharField(max_length=20)
    
    def __str__(self):
        return self.title

# Product model
class Product(models.Model):
    title=models.CharField(max_length=50)
    detail=models.TextField()
    unit=models.ForeignKey(Unit, on_delete=models.CASCADE)
    photo=models.ImageField(upload_to="product/")
    
    def __str__(self):
        return self.title
from django.db import models
import datetime
import os
from django.contrib.auth.models import User

# Create your models here.

def GetFileName (request, filename):
    now_time = datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename = "%s%s"%(now_time, filename)
    return os.path.join('uploads/', new_filename)

class category(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(max_length=500, blank=False, null=False)
    image = models.ImageField(upload_to=GetFileName, blank=False, null=False)
    status = models.BooleanField(default=False, help_text='0-Show | 1-Hidden')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
class Product(models.Model):
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False, null=False)
    venter = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(max_length=500, blank=False, null=False)
    quantity = models.IntegerField(blank=False, null=False)
    Original_price = models.IntegerField(blank=False, null=False)
    shelling_price = models.IntegerField(blank=False, null=False)
    image = models.ImageField(upload_to=GetFileName, blank=False, null=False)
    status = models.BooleanField(default=False, help_text='0-Show | 1-Hidden')
    trending = models.BooleanField(default=False, help_text='0-normal | 1-trending')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Product_qty = models.IntegerField(blank=False, null=False)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Product.name
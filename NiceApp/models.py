from django.db import models

# Create your models here.
class Categorydb(models.Model):
    CategoryName = models.CharField(max_length=50,null=True,blank=True)
    CategoryImage = models.ImageField(upload_to="profile",null=True,blank=True)

class Productdb(models.Model):
    Category = models.CharField(max_length=50,null=True,blank=True)
    ProductName = models.CharField(max_length=50,null=True,blank=True)
    Price = models.CharField(max_length=50,null=True,blank=True)
    Brand = models.CharField(max_length=50,null=True,blank=True)
    Ingredients = models.CharField(max_length=50,null=True,blank=True)
    Image = models.ImageField(upload_to="media",null=True,blank=True)

class NewsDb(models.Model):
    Name = models.CharField(max_length=50,null=True,blank=True)
    Message = models.CharField(max_length=50,null=True,blank=True)
    Image = models.ImageField(upload_to="nmedia",null=True,blank=True)







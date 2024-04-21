from django.db import models

# Create your models here.

class Contactdb(models.Model):
    Name = models.CharField(max_length=50,null=True,blank=True)
    Email = models.EmailField(max_length=50,null=True,blank=True)
    Phone = models.IntegerField(null=True,blank=True)
    Subject = models.CharField(max_length=50,null=True,blank=True)
    Message = models.CharField(max_length=50,null=True,blank=True)

class Userdb(models.Model):
    User_Name = models.CharField(max_length=50,null=True,blank=True)
    EmailId = models.EmailField(max_length=50,null=True,blank=True)
    Phone = models.IntegerField(null=True,blank=True)
    Image = models.ImageField(upload_to="userprofile",null=True,blank=True)
    Password = models.CharField(max_length=50,null=True,blank=True)


class CartDb(models.Model):
    User_Name = models.CharField(max_length=50,null=True,blank=True)
    ProductName = models.CharField(max_length=50,null=True,blank=True)
    Brand = models.CharField(max_length=50,null=True,blank=True)
    Ingredients = models.CharField(max_length=50,null=True,blank=True)
    Quantity = models.IntegerField(null=True,blank=True)
    TotalPrice = models.CharField(max_length=50,null=True,blank=True)
    Image = models.ImageField(upload_to="cmedia",null=True,blank=True)

class CheckoutDb(models.Model):
    Name = models.CharField(max_length=50,null=True,blank=True)
    Email = models.EmailField(max_length=50,null=True,blank=True)
    Address = models.CharField(max_length=50,null=True,blank=True)
    Phone = models.IntegerField(null=True,blank=True)
    Message = models.CharField(max_length=50,null=True,blank=True)


from django.db import models

class Member(models.Model):
  full_name = models.CharField(max_length=255)
  location = models.CharField(max_length=255,null=True,blank=True)
  email = models.EmailField(max_length=100,null=True,blank=True)
  property_name = models.CharField(max_length=255,null=True,blank=True)
  image_property = models.FileField(upload_to='members',max_length=255,null=True,blank=True,default=None)
  descpription = models.CharField(max_length=255,null=True,blank=True)
  bathroom = models.IntegerField(null=True,blank=True)
  price = models.IntegerField(null=True,blank=True)
  phone = models.IntegerField(null=True,blank=True)
  room = models.IntegerField(null=True,blank=True)
class contact_model(models.Model):
  email = models.EmailField(max_length=100,null=True,blank=True)
  full_name = models.CharField(max_length=255)
  subject = models.CharField(max_length=255,null=True,blank=True)
  message = models.TextField(null=True,blank=True)

def __str__(self):
    return f"{self.firstname} {self.lastname} "
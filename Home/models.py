from django.db import models

# Create your models here.
class Contact(models.Model):
    SNO = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=250)
    message = models.TextField()
    timeStamp= models.DateTimeField(auto_now_add=True, blank=True)




class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

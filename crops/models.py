from django.db import models

# Create your models here.

class Contribute(models.Model):
    Nitrogen = models.CharField(max_length=20,blank=True,null=True)
    Phosphorous = models.CharField(max_length=20,blank=True,null=True)
    Potassium = models.CharField(max_length=20,blank=True,null=True)
    Temperature = models.CharField(max_length=20,blank=True,null=True)
    Humidity = models.CharField(max_length=20,blank=True,null=True)
    Ph = models.CharField(max_length=20,blank=True,null=True)
    Rainfall = models.CharField(max_length=20,blank=True,null=True)
    Suitable_crop = models.CharField(max_length=20,blank=True,null=True)

    def __str__(self):
        return "Contribute"

    
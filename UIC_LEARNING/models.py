from django.db import models

# Create your models here.
class enrolledstudents(models.Model):
    name = models.CharField(max_length=50,null= True,blank=True)
    email = models.EmailField(null= True,blank=True,unique=True)
    password = models.CharField(max_length=50,null= True,blank= True)
    contact_number = models.IntegerField(null= True,blank=True)
    course = models.CharField(max_length=50,null= True,blank= True)


class contact(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True, unique=True)
    message = models.CharField(max_length=500, null=True, blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    
    


    
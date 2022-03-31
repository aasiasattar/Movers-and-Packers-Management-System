from io import open_code
from django.db import models
from django.db.models.fields import DateField
from django.http import request
from django.contrib.auth.models import User
# Create your models here.

class SiteUser(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    mobile = models.CharField(max_length=25, null=True)
    location = models.CharField(max_length=200, null=True)
    shifting_loc = models.CharField(max_length=200, null=True)
    shiftingdate = models.DateField(null=True)
    brief_items = models.CharField(max_length=300, null=True)
    items = models.CharField(max_length=5000, null=True)
    requestdate = models.DateField(null=True)
    remark = models.CharField(max_length=500,null=True)
    status = models.CharField(max_length=30,null=True)
    updationdate = models.DateField(null=True)

    def __str__(self):
        return self.name



    
class Services(models.Model):
    
    title = models.CharField(max_length=300, null=True)
    image = models.FileField(null=True)
    description = models.CharField(max_length=5000, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    
    name = models.CharField(max_length=100, null=True)
    subject = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=200, null=True)
    message = models.CharField(max_length=5000, null=True)
    number = models.CharField(max_length=30,null=True)
    msg_date = models.DateField(null=True)
    is_read = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.name


    
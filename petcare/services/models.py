from email.policy import default
from pyexpat import model
from secrets import choice
from site import USER_BASE
from django.db import models

# Create your models here.


from operator import mod
from sre_constants import MAX_UNTIL
from statistics import mode
from django.forms import CharField

class User(models.Model):
    ADMIN = 'AD'
    USER = 'US'
    USER_TYPES=[
        (USER,'user'),
        (ADMIN,'admin'),
    ]
    fnm = models.CharField(max_length=127)
    lnm = models.CharField(max_length=127)
    unm = models.CharField(max_length=127,primary_key=True)
    email = models.CharField(max_length=255)
    pno = models.CharField(max_length=127)
    password = models.CharField(max_length=127)
    role = models.CharField(max_length=127,choices=USER_TYPES,default='user')
    date = models.DateTimeField(auto_now=True)

class Pet(models.Model):
    name = models.CharField(max_length=127)
    breed = models.CharField(max_length=127)
    color = models.CharField(max_length=127)
    age = models.CharField(max_length=127)
    size = models.CharField(max_length=127)
    weight = models.CharField(max_length=127)
    gender = models.CharField(max_length=127)
    image = models.ImageField(upload_to = 'upload/')
    addedby = models.CharField(max_length=127)
    date = models.DateTimeField(auto_now=True)

class Volunteer(models.Model):
    fnm = models.CharField(max_length=127)
    lnm = models.CharField(max_length=127)
    unm = models.ForeignKey(User,on_delete=models.CASCADE)
    email = models.CharField(max_length=127, primary_key=True)
    pno = models.CharField(max_length=127)
    address = models.CharField(max_length=127)
    date = models.DateTimeField(auto_now=True)

class Adoption(models.Model):
    unm = models.ForeignKey(User,on_delete=models.CASCADE)
    pid = models.ForeignKey(Pet,on_delete=models.CASCADE)
    email = models.CharField(max_length=127)
    pno = models.CharField(max_length=127)
    address = models.CharField(max_length=127)
    date = models.DateTimeField(auto_now=True)
    approve = models.BooleanField(default=False)

class Feedback(models.Model):
    name = models.CharField(max_length=127)
    email = models.CharField(max_length=127)
    message = models.TextField()
    date = models.DateTimeField(auto_now=True)
    enable = models.BooleanField(default=False)
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
import datetime

# Create your models here

class CustomUser(AbstractUser):
    fname = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    public_visibility = models.BooleanField(default=True)
    birth_date = models.DateField(null=True)
    age = models.PositiveIntegerField(null=True)
    location = models.TextField(null=True)

# from django.contrib.auth.models import User
class Details(models.Model):
    uname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    fullname = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    public_visibility = models.BooleanField(default=True)
    birth_date = models.DateField(null=True)
    location = models.TextField(null=True)

    def __str__(self):
        return self.uname

class uploaded_files(models.Model):
    Title = models.CharField(max_length=200)
    Description = models.TextField()
    Visibility = models.BooleanField(default=False)
    Cost = models.PositiveIntegerField(null=True)
    Year = models.SmallIntegerField(null=True)
    Cover = models.ImageField(upload_to="media/image/")
    Book = models.FileField(upload_to="media/pdf/")

    def __str__(self):
        return self.Title

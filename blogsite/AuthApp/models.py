from django.db import models
from .managers import *
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin



   # Your custom user manager implementation here

GENDER_CHOICES = (
    ('Male','Male'),
    ('Female' , 'Female'),
    ('Other','Other'),
)
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=244, unique=True, null=True)
    email = models.EmailField(('email_address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    first_name = models.CharField(max_length=44 , null=True , blank=True)
    last_name = models.CharField(max_length=44 , null= True , blank=True)
    gender = models.CharField(max_length=44,choices = GENDER_CHOICES , null=True)
    number = models.CharField(max_length=10 , null=True)
    profile = models.ImageField(upload_to='images',null=True)
    

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return self.username
    
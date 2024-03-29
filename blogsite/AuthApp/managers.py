from django.contrib.auth.models import BaseUserManager
from .models import *


class CustomUserManager(BaseUserManager):

    def create_user(self,email,username,password,**extra_fields):
        if not email:
            raise ValueError(('The email must be set'))
        email = self.normalize_email(email)
        username = username
        user = self.model(email=email,username=username,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    
    def create_superuser(self,email,username,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError(('superuser must have is_staff = True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('superuser must have is_superuser = True'))
        if extra_fields.get('is_active') is not True:
            raise ValueError(('superuser must have is_active = True'))
        return self.create_user(email,username,password,**extra_fields)
        
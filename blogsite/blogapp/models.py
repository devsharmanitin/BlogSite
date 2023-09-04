# Create your models here.
from django.db import models
from cloudinary.models import CloudinaryField
from AuthApp.models import CustomUser

    
class tag(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

class blog(models.Model):
    heading = models.CharField(max_length=50)
    image = CloudinaryField('image')
    desc = models.TextField(max_length=1000000)
    upload_on = models.CharField(max_length=50)
    upload_by = models.CharField(max_length=100)
    datefield = models.DateField(auto_now_add=True)
    tag = models.ForeignKey(tag,on_delete=models.CASCADE,null=True)
    likes = models.PositiveIntegerField(default=0 , null=True , blank=True)
    
    def __str__(self):
        return self.heading

class Like(models.Model):
    blog = models.ForeignKey(blog , on_delete=models.CASCADE , null=True)
    user = models.ForeignKey(CustomUser , on_delete=models.CASCADE , null=True) 


class Comments(models.Model):
    user = models.ForeignKey(CustomUser , on_delete=models.CASCADE , null=True , blank=True)
    blog = models.ForeignKey(blog , on_delete=models.CASCADE , null=True)
    comment = models.CharField(max_length=300 , null=True , blank=True)
    parent_comment = models.ForeignKey('self' , on_delete=models.CASCADE , null=True , blank=True , related_name='reply')
    timedata = models.DateTimeField(auto_now_add=True , null=True)
    
    def __str__(self):
        return self.comment    
    
class Contact(models.Model):
    FirstName = models.CharField(max_length=100 )
    LastName = models.CharField(max_length=100)
    email = models.EmailField('email_address')
    Feedback = models.CharField(max_length=10000)
    user_name =  models.ForeignKey(CustomUser , on_delete=models.CASCADE )
    
    def __str__(self):
        return self.user_name.username
     
    
    
    

    
    

    
    
    
    
    
    
    


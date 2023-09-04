from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import *
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        models = CustomUser
        fields = ['email' , 'username']
        
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = ['email','username']
        
class CustomUserDataForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect)
    number = forms.IntegerField(widget=forms.NumberInput ,)
    class Meta:
        model = CustomUser
        fields = ['email','first_name' ,'last_name'  ,'number' , 'gender']
        
class UserProfileUpdate(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('profile',)
    

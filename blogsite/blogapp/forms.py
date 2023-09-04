from django import forms
from .models import *
from django.forms.widgets import TextInput,EmailInput,NumberInput,DateInput
# from phonenumber_field.formfields import PhoneNumberField

class blogform(forms.ModelForm):
    class Meta:
        model = blog
        fields = "__all__"
        
        
    def __init__(self,*args,**kwargs):
        super(blogform,self).__init__(*args,**kwargs)
        self.fields['tag'].empty_label = "select tag"
        
        self.fields['heading'].widget.attrs.update({'class':'form-control form-control-lg' , 'id': 'form3Example1m'})


class CommentForm(forms.ModelForm):
    parent_comment = forms.IntegerField(widget=forms.HiddenInput, required=False)
    class Meta:
        model = Comments
        fields = "__all__"
        
    def __init__(self , *args , **kwargs):
        super(CommentForm , self).__init__(*args , **kwargs)
        self.fields['user'].required = False
        self.fields['blog'].required = False
        
        
class CommentUpdateForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comment',)
        widgets = {
            'comment': forms.TextInput(attrs={'class': 'form-control',  'rows': 4}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        
        
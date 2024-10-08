from django import forms 
from django.core import validators
from .models import user

class FormValid(forms.ModelForm):
     class Meta:
        model = user
        fields = ['name','email','password','Rpassword']


     
 
        
       

   
   





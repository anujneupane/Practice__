from django import forms 
from django.core import validators
from .models import user

class FormValid(forms.ModelForm):
     class Meta:
        
        model = user
        fields = ['name','email','password','Rpassword']
        labels = {'name':'Enter name',
                  'email' : 'Enter email',
                  'password' : 'Enter password',
                  'Rpassword' : 'Retype password',
                  }
        error_messages = {
            'name' : {'required':'Input your Full name'},
            'email' : {'required':'Input your Email'},
            'password' : {'required':'Input your Password'},
            }
        widgets = { 'password' : forms.PasswordInput ,
                   'Rpassword' : forms.PasswordInput
                   
                   }






     
  
        
       

   
   





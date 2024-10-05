from django import forms 
from django.core import validators
 
def start_with_a(value):
    if value[0] != 'a':
        raise forms.ValidationError('Name must be started with a')

class FormValid(forms.Form):
     name = forms.CharField(validators = [start_with_a])
     email = forms.EmailField()
   
 
        
       

   
   





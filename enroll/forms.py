from django import forms 
from django.core import validators
 
class FormValid(forms.Form):
     name = forms.CharField()
     email = forms.EmailField()
     password = forms.CharField(widget=forms.PasswordInput)
     rpassword = forms.CharField(label='Password(Retype)',widget=forms.PasswordInput)


def clean(self):
    cleaned_data = super().clean()
    pwd = self.cleaned_data['password']
    rpwd = self.cleaned_data['rpassword']
    if pwd != rpwd:  
      raise forms.ValidationError('Passwords do not match')
    return cleaned_data

 
        
       

   
   





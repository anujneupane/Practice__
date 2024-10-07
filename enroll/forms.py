from django import forms 
from django.core import validators
 
class FormValid(forms.Form):
     error_css_class = 'error'
     required_css_class = 'required'
     name = forms.CharField(error_messages={'required' : 'Enter your Name'})
     email = forms.EmailField(error_messages={'required': 'Enter your Email'})
     password = forms.CharField(widget=forms.PasswordInput)
     rpassword = forms.CharField(label='Password(Retype)',widget=forms.PasswordInput)


     def clean(self):
       cleaned_data = super().clean()
       print(type(cleaned_data))  # Debug print to check type
       pwd = cleaned_data.get('password')
       rpwd = cleaned_data.get('rpassword')
       if pwd and rpwd and pwd != rpwd:  
        raise forms.ValidationError('Passwords do not match')
       return cleaned_data
 
        
       

   
   





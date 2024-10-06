from django.shortcuts import render
from .forms import FormValid

# Create your views here.


def valid(request):
    if request.method == 'POST':
        fm = FormValid(request.POST)
        if fm.is_valid():
            print('Form validated')
            print('name:',fm.cleaned_data ['name'])
            print('email:',fm.cleaned_data ['email'])
            print('Password:',fm.cleaned_data ['password'])
            print('Rpassword:',fm.cleaned_data ['rpassword'])
            fm = FormValid()
            
    else:
     fm = FormValid() #form for GET request
        
    return render(request,'enroll/form2.html',{'form':fm})
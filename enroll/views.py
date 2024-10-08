from django.shortcuts import render,redirect
from .forms import FormValid

# Create your views here.


def valid(request):
    if request.method == 'POST':
        fm = FormValid(request.POST)
        if fm.is_valid():
            
           name      = fm.cleaned_data ['name']
           email     = fm.cleaned_data ['email']
           password  = fm.cleaned_data ['password']
           Rpassword = fm.cleaned_data ['Rpassword']
           print(name)
           print(email)
           print(password)
           print(Rpassword)
             
    else:
        fm = FormValid() #form for GET request
        
    return render(request,'enroll/form2.html',{'form':fm})  
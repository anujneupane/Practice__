from django.shortcuts import render
from .forms import FormValid
from .models import user

# Create your views here.


def valid(request):
    if request.method == 'POST':
        fm = FormValid(request.POST)
        if fm.is_valid():
            
           name      = fm.cleaned_data ['name']
           email     = fm.cleaned_data ['email']
           password  = fm.cleaned_data ['password']
           Rpassword = fm.cleaned_data ['Rpassword']
           reg = user(name = name, email = email,password = password, Rpassword = Rpassword)
           reg.save()
          
           fm = FormValid()
             
    else:
        fm = FormValid() #form for GET request
        
    return render(request,'enroll/form2.html',{'form':fm})   
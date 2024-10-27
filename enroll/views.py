from django.shortcuts import render

def home(request,status):
    print(status)
    return render(request,'enroll/home.html')

def valid(request,my_id): 
 if my_id == 1:
     employee = { 'id' : my_id, 'name': 'Manish'}
 if my_id == 2:
     employee = { 'id' : my_id, 'name': 'Baibhav'}
 if my_id == 3:
     employee = { 'id' : my_id, 'name': 'Aaku'}
 return render(request,'enroll/form2.html', employee)

from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def first(request):
    
    emp = Employee.objects.all()
    context = {
        'emp': emp    
        }
    return render(request,'emp.html', context)

def add(request):    
    if request.method == 'POST':
        name = request.POST.get('name')        
        email = request.POST.get('email')
        address = request.POST.get('address')        
        phone = request.POST.get('phone')
        designation = request.POST.get('designation')
        
    emp = Employee (
        name=name,
        email=email,
        address=address,
        phone=phone,
        designation=designation,
        )
           
    emp.save()
    return render(request,'emp.html')

def edit(request, id):
    emp=Employee.objects.all()
    context = {
           'emp':emp
           }
    return render("emp.html", context)

def delete(request, id):
    emp = Employee.objects.filter(id=id)
    emp.delete()
    return render(request, "emp.html")

def update(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')        
        email = request.POST.get('email')
        address = request.POST.get('address')        
        phone = request.POST.get('phone')
        designation = request.POST.get('designation')
        
    emp = Employee (
        name=name,
        email=email,
        address=address,
        phone=phone,
        designation=designation,
        )
           
    emp.save()
    return render(request,'emp.html')

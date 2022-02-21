from django.shortcuts import render,redirect
from.models import *
from .forms import *
from django.contrib import auth
from contact.forms import *

# Create your views here.


def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
    try:
        user = Customer.objects.get(email=email, password=password)
        if user is not None:
            return redirect('mainpage')
        else:
            print("Login Invalid")
            return redirect("customer/register/")
    except:
        return render(request, 'Customer/login.html')


def home(request):
    return render(request, 'index.html')

def products(request):
    return render(request,'products2.html')

def contact(request):
    if request.method == "POST":
        form = ContactForms(request.POST)
        if form.is_valid():
            form.save()
           
            return redirect("/mainpage/")
        else:
    
            return redirect("/contact/")
    return render(request,'contact.html')

def mainpage(request):
    return render(request, 'base.html')  

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method == "POST":
        form = CustomerForms(request.POST)
        if form.is_valid():
            form.save()
            print("Register successFul")
            return redirect("/customer/login/")
        else:
            print("Data Invalid")
            return redirect("/customer/register/")
    return render(request, 'Customer/register.html')

def converse(request):
    return render(request,'converse.html')

def adidas(request):
    return render(request,'adidas.html')

def nike(request):
    return render(request,'nike.html')





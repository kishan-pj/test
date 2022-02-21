from django.shortcuts import render,redirect
from Customer.views import contact
from products.forms import ProductForms, BookingForms
from products.models import Products,Cartproducts
from contact.models import Contact
from contact.forms import ContactForms

# Create your views here.
def product_form(request):
    if request.method == "POST":
        form = ProductForms(request.POST,request.FILES)
        
        form.save()
        print("Register successFul")
        return redirect("mainpage/")
        
           
    return render(request,'product_form.html')

def details(request):
    Nikes=Products.objects.filter(product_type='nike')
    adidas=Products.objects.filter(product_type='adidas')
    converse=Products.objects.filter(product_type='converse')

    return render(request,'products2.html',{'Nikes':Nikes,'adidas':adidas,'converse':converse})

def cart(request,p_id):
    if request.method == "POST":
        form = BookingForms(request.POST)
        if form.is_valid():
            form.save()
            print('productbooked')
            return redirect("/cartdetails")
        else:
            print("Data Invalid")
            return redirect("/cart")
    
    
    products=Products.objects.get(product_id=p_id)

    return render(request,"cart.html",{'products':products})

def contactdetails(request):
    contacts=Contact.objects.all()

    return render(request,'contactdetails.html',{'contacts':contacts})

def editdetails(request,p_id):
    customer=Contact.objects.get(customer_id=p_id)
    return render(request,"edit.html",{'customer':customer})

def deleteuser(request,p_id):
    try:
       user=Contact.objects.get(customer_id=p_id)
       user.delete()

    except:

        print("No data Found")

    return redirect("/contactdetails")

def updateuser(request,p_id):

    user = Contact.objects.get(customer_id=p_id)

    form = ContactForms(request.POST, instance=user)

    if form.is_valid():

        try:

           form. save()

           return redirect("/user/viewuser")

        except:

           print("validation failed")

    return render(request, "admin/edituser.html", {'users':user})

def view(request):
    return render(request,'view.html')

def addproduct(request):
    return render(request,'product_form.html')

# def seeorder(request):
#     booking = Cartproducts.objects.all()
#     return render(request, 'orderdetails.html',{'booking':booking})
from django.shortcuts import render
from django.http import HttpResponse
from app_core.models import Category, Delivery, District, Location, Smoothie
from django.contrib.auth import authenticate,login
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib.auth import logout

from app_dashboard.models import Customer
from count_your_calories.users.models import User

# Create your views here.
def appdash(request):
    return render(request, "admin_dashboard.html")
def index(request):
    s=Smoothie.objects.all()
    return render (request, "index.html",{"c":s})
def log(request):
    if request.method == 'POST':
        uname=request.POST.get("uname")
        passwd=request.POST.get("passwd")
        user=authenticate(request,username=uname,password=passwd)
        if user is not None:
            login(request,user)
            if user.role == 'Admin':
                return HttpResponse ("<script>alert('Login sucessfull');window.location='/adm/';</script>")
            elif user.role == 'customer':
                return HttpResponse ("<script>alert('Login sucessfull');window.location='/core/cust_smoothie/';</script>")
            elif user.role == 'delivery':
                d=Delivery.objects.get(user=user)
                if d.status=="accept":
                    return HttpResponse ("<script>alert('Login sucessfull');window.location='/customerdash/';</script>")
                else:
                    return HttpResponse ("<script>alert('Login unsucessfull');window.location='/log/';</script>")
        else:
            return HttpResponse ("<script>alert('Login unsucessfull');window.location='/log/';</script>")
    return render (request, "login.html")


def guest(request):
    return render (request, "login.html")

def customer_reg(request):
    if request.method=="POST":
        name=request.POST.get("name")
        address=request.POST.get("address")
        height=request.POST.get("height")
        weight=request.POST.get("weight")
        age=request.POST.get("age")
        uname=request.POST.get("uname")
        passwd=request.POST.get("passwd")
        email=request.POST.get("mail")
        contact_no=request.POST.get("contact")
        gender=request.POST.get("gender")
        location=request.POST.get("loc")
        if User.objects.filter(username=uname).exists():
            return HttpResponse("<script>alert('Already Exist');window.location='/reg';</script>")
        u=User()
        u.name=name
        u.username=uname
        u.set_password(passwd)
        u.email=email
        u.role="customer"
        u.save()
        
        c=Customer()
        c.address=address
        c.location=location
        c.contact=contact_no
        c.age=age
        c.height=height
        c.weight=weight
        c.user=User.objects.get(username=uname)
        c.save()
        send_mail(subject="Registation Sucessfull", message=f"hi {name},\n welcome to Count your Calories" ,from_email=None,recipient_list=[email])
        return HttpResponse("<script>alert('Insertion sucessfull');window.location='/reg';</script>")
    else:
        return render(request, "c_registration.html")


def customer_dash(request):
    s=Smoothie.objects.all()
    return render (request, "customer_dash.html",{"cust":s})

def delv_dash(request):
    return render (request, "delivery_dash.html")
    
    
def logout_view(request):
    logout(request)
    return HttpResponse("<script>alert('Logged out successfully');window.location='/log/';</script>")
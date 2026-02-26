from django.shortcuts import render
from django.http import HttpResponse
from app_core.models import Cart, Category, Delivery, District, Location, Smoothie
from django.contrib.auth import authenticate,login
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib.auth import logout
from django.db.models import Count

from app_dashboard.models import Customer
from count_your_calories.users.models import User

# Create your views here.

def appdash(request):

    smoothie_data = (
        Cart.objects.values('smoothie__name')
        .annotate(booking_count=Count('master_id', distinct=True))
        .order_by('-booking_count')
    )

    labels = [item['smoothie__name'] for item in smoothie_data if item['smoothie__name']]
    data = [item['booking_count'] for item in smoothie_data if item['smoothie__name']]

    seller_data = (
        Cart.objects.values('customer__name')
        .annotate(booking_count=Count('master_id', distinct=True))
        .order_by('-booking_count')
    )

    lab = [item['customer__name'] for item in seller_data if item['customer__name']]
    dat = [item['booking_count'] for item in seller_data if item['customer__name']]

    context = {
        'labels': labels,
        'data': data,
        'lab': lab,
        'dat': dat,
    }

    return render(request, 'admin_dashboard.html', context)

def index(request):
    s = Smoothie.objects.all()

    top_smoothies = (
        Cart.objects
        .annotate(total_bookings=Count('master_id', distinct=True))
        .order_by('-total_bookings')[:5]
    )
    return render(request, "Customer_dash.html", {"c": s,"top": top_smoothies})

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
    return HttpResponse("<script>alert('Logged out successfully');window.location='/customerdash/';</script>")
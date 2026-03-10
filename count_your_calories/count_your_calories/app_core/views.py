from datetime import date
import json
import random
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Avg, Count, Sum
from app_core.models import Booking, Cart, Category, CustomBooking, CustomIngredients, Delivery, Deliveryupdate, District, Favourite, Ingredients, Location,Payment, Rating, Review, Smoothie
from app_dashboard.models import Customer, Deliverydetails
from count_your_calories.users.models import User
from django.http import JsonResponse
from django.template.loader import render_to_string

#from count_your_calories.app_dashboard.models import customer
#from count_your_calories.users.models import User

# def dis_entry(request):
#     if request.method=="POST":
#         d=request.POST.get("name")
#         print(d)
#         if District.objects.filter(name=d).exists():
#             # print ("hi")
#             return HttpResponse("<script>alert('Already Exist');window.location='/core/district';</script>")
#         cat=District()
#         cat.name=d
#         cat.save()
#         return HttpResponse("<script>alert('Insertion sucessfull');window.location='/core/district';</script>")
#     else:
#         return render (request, "district.html")
    
# def dis_view(request):
#     d=District.objects.all()
#     print (d)
#     return render (request, "disview.html",{"data":d})


# def dis_del(request,no):
#     d=District.objects.get(id=no)
#     d.delete()
#     return HttpResponse("<script>alert('Deletion sucessfull');window.location='/home/dv';</script>")

# def dis_upd(request,no):
    # u=District.objects.get(id=no)
    # if request.method=="POST":
    #     ca=request.POST.get("name")
    #     if District.objects.filter(name=ca).exists():
    #         # print ("hi")
    #         return HttpResponse("<script>alert('Already Exist');window.location='/home/dv/';</script>")
    #     u.name=ca
    #     u.save()
    #     return HttpResponse("<script>alert('Updation sucessfull');window.location='/home/dv/';</script>")
    # return render(request, "admin/editdis.html",{"vi":u})


def loc_entry(request):
    if request.method=="POST":
        n=request.POST.get("name")
        d_id=request.POST.get("dis")
        if Location.objects.filter(name=n,district=d_id).exists():
            # print ("hi")
            return HttpResponse("<script>alert('Already Exist');window.location='/core/location';</script>")
        cat=Location()
        cat.name=n
        cat.district=District.objects.get(id=d_id)
        cat.save()
        return HttpResponse("<script>alert('Insertion sucessfull');window.location='/core/location';</script>")
    else:
        d=District.objects.all()
        return render(request, "location.html",{"d_val":d})

def loc_view(request):
    l=Location.objects.all()
    return render (request, "locview.html",{"ldata":l})

def loc_del(request,no):#delete
    d=Location.objects.get(id=no)
    d.delete()
    return HttpResponse ("<script>alert('Deletion sucessfull');window.location='/core/locview';</script>")

def loc_upd(request,no):#update
    #return HttpResponse("<script>alert('updated sucessfull');window.location='/home/cav';</script>")
    d=Location.objects.get(id=no)
    if request.method=="POST":
        ca=request.POST.get("name")
        des=request.POST.get("dis")
        if Location.objects.filter(name=ca,district=des).exists():
            return HttpResponse("<script>alert('Already Exist');window.location='/core/locview';</script>")
        d.name=ca
        d.district=District.objects.get(id=des)
        d.save()
        return HttpResponse("<script>alert('Updation sucessfull');window.location='/core/locview/';</script>")
    else:
        dis=District.objects.all()
        return render(request, "locedit.html",{"lupd":d,'dist':dis})
    
def cat_entry(request):
    if request.method=="POST":
        name=request.POST.get("name")
        desc=request.POST.get("des")
        if Category.objects.filter(name=id).exists():
            # print ("hi")
            return HttpResponse("<script>alert('Already Exist');window.location='/core/category';</script>")
        cat=Category()
        cat.name=name
        cat.desc=desc
        cat.save()
        return HttpResponse("<script>alert('Insertion sucessfull');window.location='/core/category';</script>")
    else:
        return render (request, "category.html")
    
def cat_view(request):
    l=Category.objects.all()
    return render (request, "catview.html",{"catdata":l})

def cat_del(request,no):#delete
    d=Category.objects.get(id=no)
    d.delete()
    return HttpResponse ("<script>alert('Deletion sucessfull');window.location='/core/catview';</script>")

def cat_upd(request,no):#update
    #return HttpResponse("<script>alert('updated sucessfull');window.location='/home/cav';</script>")
    d=Category.objects.get(id=no)
    if request.method=="POST":
        ca=request.POST.get("name")
        des=request.POST.get("des")
        if Category.objects.filter(name=ca).exclude(id=no).exists():
            return HttpResponse("<script>alert('Already Exist');window.location='/core/catview/';</script>")
        d.name=ca
        d.desc=des
        d.save()
        return HttpResponse("<script>alert('Updation sucessfull');window.location='/core/catview/';</script>")
    else:
        dis=District.objects.all()
        return render(request, "editcategory.html",{"v":d})

def card(request):
    l=Category.objects.all()
    return render (request, "card.html",{"card_val":l})

def ing_entry(request):
    if request.method=="POST":
        name=request.POST.get("name")
        avail=request.POST.get("avail")
        price=request.POST.get("price")
        calorie=request.POST.get("calorie")
        if Ingredients.objects.filter(name=name).exists():
            return HttpResponse("<script>alert('Already Exist');window.location='/core/ingredients';</script>")
        ing=Ingredients()
        ing.name=name
        ing.availability=avail
        ing.price=price
        ing.calorie=calorie
        if len(request.FILES) !=0:
            cimg=request.FILES['cimg']
            ing.simg=cimg
        ing.save()
        return HttpResponse("<script>alert('Insertion sucessfull');window.location='/core/ingredients';</script>")
    else:
        return render (request, "ingredients.html")
    
def ing_view(request):
    l=Ingredients.objects.all()
    return render (request, "ingview.html",{"ingdata":l})

def ing_del(request,no):#delete
    d=Ingredients.objects.get(id=no)
    d.delete()
    return HttpResponse ("<script>alert('Deletion sucessfull');window.location='/core/ing_view';</script>")

def ing_upd(request,no):#update
    #return HttpResponse("<script>alert('updated sucessfull');window.location='/home/cav';</script>")
    d=Ingredients.objects.get(id=no)
    if request.method=="POST":
        name=request.POST.get("name")
        avail=request.POST.get("avail")
        price=request.POST.get("price")
        if Ingredients.objects.filter(name=name).exclude(id=no).exists():
            return HttpResponse("<script>alert('Already Exist');window.location='/core/ing_view/';</script>")
        d.name=name
        d.availability=avail
        d.price=price
        calorie=request.POST.get("calorie")
        d.calorie=calorie
        if len(request.FILES) !=0:
            cimg=request.FILES['cimg']
            d.simg=cimg
        d.save()
        return HttpResponse("<script>alert('Updation sucessfull');window.location='/core/ing_view/';</script>")
    else:
        return render(request, "ingupd.html",{"i":d})
    
def smoothie_entry(request):
    if request.method=="POST":
        name=request.POST.get("name")
        ingr=request.POST.getlist("ing[]")
        avail=request.POST.get("avail")
        price=request.POST.get("price")
        #print(ing)
        if Smoothie.objects.filter(name=name).exists():
            return HttpResponse("<script>alert('Already Exist');window.location='/core/smoothie';</script>")
        ing=Smoothie()
        ing.name=name
        ing.availability=avail
        if len(request.FILES) !=0:
            cimg=request.FILES['cimg']
            ing.simg=cimg
        ing.price=price
        ing.save()
        for i in ingr:
            ing.ingredients.add(i)
        return HttpResponse("<script>alert('Insertion sucessfull');window.location='/core/smoothie';</script>")
    else:
        i=Ingredients.objects.all()
        return render (request, "smoothie.html",{"ival":i})
    
def smoothie_view(request):
    l=Smoothie.objects.all()
    return render (request, "smoothieview.html",{"smoothiedata":l})

def smoothie_del(request,no):#delete
    d=Smoothie.objects.get(id=no)
    d.delete()
    return HttpResponse ("<script>alert('Deletion sucessfull');window.location='/core/smoothie_view';</script>")

def smoothie_upd(request,no):#update
    #return HttpResponse("<script>alert('updated sucessfull');window.location='/home/cav';</script>")
    d=Smoothie.objects.get(id=no)
    ingredients = Ingredients.objects.all()
    if request.method=="POST":
        name=request.POST.get("name")
        ings=request.POST.getlist("ing[]")
        avail=request.POST.get("avai")
        calorie=request.POST.get("calorie")
        price=request.POST.get("price")
        if Smoothie.objects.filter(name=name).exclude(id=no).exists():
            return HttpResponse("<script>alert('Already Exist');window.location='/core/smoothie_view/';</script>")
        d.name=name
        d.availability=avail
        d.price=price
        d.calorie=calorie
        d.save()
        for i in ings:
            d.ingredients.add(i)
        return HttpResponse("<script>alert('Updation sucessfull');window.location='/core/smoothie_view/';</script>")
    else:
        return render(request, "smoothieupd.html",{"s_upd":d,"ingredients":ingredients})
    
def c_view(request):
    l=Customer.objects.all()
    return render (request, "customerview.html",{"cdata":l})

def delivery_reg(request):
    if request.method=="POST":
        name=request.POST.get("name")
        uname=request.POST.get("uname")
        passwd=request.POST.get("passwd")
        mail=request.POST.get("mail")
        contact_no=request.POST.get("contact")
        l_no=request.POST.get("l_no")
        if User.objects.filter(username=uname).exists():
            return HttpResponse("<script>alert('Already Exist');window.location='/core/delivery_reg';</script>")
        u=User()
        u.name=name
        u.username=uname
        u.set_password(passwd)
        u.email=mail
        u.role="delivery"
        u.save()

        d=Delivery()
        d.contact=contact_no
        d.licence_no=l_no
        d.user=User.objects.get(username=uname)
        d.save()
        return HttpResponse("<script>alert('Insertion sucessfull');window.location='/core/delivery_reg';</script>")
    else:
        return render(request, "delivery_reg.html")
    
def delv_view(request):
    l=Delivery.objects.filter(status="processing")
    return render (request, "delivery_view.html",{"delv_data":l})
    
def delv_acpt(request,no):
    d=Delivery.objects.get(id=no)
    d.status="accept"
    d.save()
    return HttpResponse ("<script>alert('Accepted sucessfully');window.location='/core/delivery_view';</script>")

def delv_rgct(request,no):
    d=Delivery.objects.get(id=no)
    d.status="reject"
    d.save()
    return HttpResponse ("<script>alert('Rejected sucessfully');window.location='/core/delivery_view';</script>")

def delv_v(request):
    l=Delivery.objects.filter(status="accept")
    return render (request, "delvv.html",{"dv":l})

# 
def cust_smoothieview(request):
    # Category filtering
    
    s = Smoothie.objects.all().annotate(avg_rating=Avg('review__rating'))
    
    category = request.GET.get('category')
    search=request.GET.get('search')
    sort = request.GET.get('sort')
    if search:
        s = s.filter(name__icontains=search)
    if category:
        s = s.filter(category_id=category)
    
    if sort == "price_asc":
        s = s.order_by('price')
    elif sort == "price_desc":
        s = s.order_by('-price')
    elif sort == "calorie_asc":
        s = s.order_by('calorie')
    elif sort == "calorie_desc":
        s = s.order_by('-calorie')
    # Add to cart
    if request.method == "POST":
        quantity = request.POST.get("quantity")
        id = request.POST.get("id")
        price = request.POST.get("price")

        c = Cart()
        c.customer = request.user
        c.smoothie = Smoothie.objects.get(id=id)
        c.quantity = quantity
        c.amount = int(price) * int(quantity)
        c.save()

    # Cart details
    cr = Cart.objects.filter(customer=request.user, master_id__isnull=True)
    cn = cr.count()
    total_amount = cr.aggregate(total=Sum('amount'))['total'] or 0
    category=Category.objects.all()
    # AJAX request
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string(
            'product_grid.html',
            {'custsview': s},
            request=request
        )
        return JsonResponse({'html': html})

    # Normal page load
    return render(
        request,
        "customer_smoothie.html",
        {
            "category":category,
            "custsview": s,
            "cart": cr,
            "count": cn,
            "total": total_amount
        }
    )

def custz_smoothie(request):
    i=Ingredients.objects.all()
    search=request.GET.get('search')
    sort = request.GET.get('sort')

    if search:
        i = i.filter(name__icontains=search)
        
    if sort == "price_asc":
        i = i.order_by('price')

    elif sort == "price_desc":
        i= i.order_by('-price')

    elif sort == "calorie_asc":
        i = i.order_by('calorie')

    elif sort == "calorie_desc":
        i = i.order_by('-calorie')

    if request.method=="POST":
        quantity=request.POST.get("quantity")
        id=request.POST.get("id")
        product = Ingredients.objects.get(id=id)

        c=CustomIngredients()
        c.customer=request.user
        c.ingredients=Ingredients.objects.get(id=id)
        c.quantity=quantity
        c.price=(int(product.price)*(int(quantity)/100))
        # c.calorie = product.calorie * quantity/100
        c.save()

    cr=CustomIngredients.objects.filter(customer=request.user,customMaster_id__isnull=True)
    cn=CustomIngredients.objects.filter(customer=request.user,customMaster_id__isnull=True).count()
    total_amount = cr.aggregate(total=Sum('price'))['total'] or 0
    return render (request, "customize_smoothie.html",{"custzview":i,"cr":cr,"cn":cn,"t":total_amount})
    
def add_fav(request,no):
    f=Favourite()
    f.customer=request.user
    f.smoothie=Smoothie.objects.get(id=no)
    f.save()
    return HttpResponse("<script>alert('added to fav');window.location='/core/cust_smoothie';</script>")

def fav(request):
    f=Favourite.objects.filter(customer=request.user)
    cn=Favourite.objects.filter(customer=request.user).count()
    return render (request, "favorite.html",{"f":f,"cn":cn})

def booking(request,type):
    request.session["type"]=type
    try:
        delivery=Deliverydetails.objects.get(customer__user=request.user)
    except:
        delivery=""
    if request.method=="POST":
        

        address=request.POST.get("address")
        loc=request.POST.get("location")
        con=request.POST.get("contact")
        pin=request.POST.get("pincode")
        d=Deliverydetails.objects.get(customer__user=request.user)
        if d:
            d.address=address
            d.location=loc
            d.contact=con
            d.pincode=pin
            d.save()
        else:
            d=Deliverydetails()
            d.address=address
            d.location=loc
            d.contact=con
            d.pincode=pin
            d.customer=Customer.objects.get(user=request.user)
            d.save()
        return HttpResponse("<script>alert('procceed to payment');window.location='/core/payment';</script>")


    if type=="cart":
        c=Customer.objects.get(user=request.user)
        dat=date.today()
        cr=Cart.objects.filter(customer=request.user,master_id__isnull=True)
        total_amount = cr.aggregate(total=Sum('amount'))['total'] or 0
        return render (request, "booking.html",{"c":c,"d":dat,"t":total_amount,"type":type,"delivery":delivery})
    elif type=="custom":
        c=Customer.objects.get(user=request.user)
        dat=date.today()
        cr=CustomIngredients.objects.filter(customer=request.user,customMaster_id__isnull=True)
        total_amount = cr.aggregate(total=Sum('price'))['total'] or 0
        return render (request, "booking.html",{"c":c,"d":dat,"t":total_amount,"type":type,"delivery":delivery})
    else:
        return HttpResponse("<script>alert('Invalid input');window.location='/core/cust_smoothie';</script>")
        

def payment(request):
    # c=Customer.objects.get(user=request.user)
    delivery=Deliverydetails.objects.get(customer__user=request.user)
    type=request.session.get("type")
    busy_delivery_ids = Deliveryupdate.objects.filter(
                status__in=["assigned", "inprogress"]
                ).values_list("delivery_id", flat=True)
    available_deliveries = Delivery.objects.exclude(id__in=busy_delivery_ids)
    if type=="cart":
        cr=Cart.objects.filter(customer=request.user,master_id__isnull=True)
        total_amount = cr.aggregate(total=Sum('amount'))['total'] or 0
        if request.method=="POST":
            b=Booking()
            b.customer=request.user
            b.date=date.today()
            b.total_amount=total_amount
            b.status="sucessfull"
            b.save()

            cr=Cart.objects.filter(customer=request.user,master_id__isnull=True)
            for i in cr:
                i.master_id=b
                i.save()
        
            p=Payment()
            p.date=date.today()
            p.master_id=b
            p.amount=total_amount
            p.type="cart"
            p.save()
            
            if available_deliveries.exists():
                random_delivery = random.choice(list(available_deliveries))

                Deliveryupdate.objects.create(
                    date=date.today(),
                    master_id=b,          # booking object
                    delivery=random_delivery,
                    type="cart",
                    status="assigned"
                )
            return HttpResponse("<script>alert('Payment Sucessfull');window.location='/core/cust_smoothie';</script>")
        return render (request, "payment.html",{"t":total_amount,"delivery":delivery})
    
    else:
        cr=CustomIngredients.objects.filter(customer=request.user,customMaster_id__isnull=True)
        total_amount = cr.aggregate(total=Sum('price'))['total'] or 0
        if request.method=="POST":
            b=CustomBooking()
            b.customer=request.user
            b.date=date.today()
            b.total_amount=total_amount
            b.status="sucessfull"
            b.save()

            cr=CustomIngredients.objects.filter(customer=request.user,customMaster_id__isnull=True)
            for i in cr:
                i.customMaster_id=b
                i.save()
        
            p=Payment()
            p.date=date.today()
            p.customMaster_id=b
            p.amount=total_amount
            p.type="custom"
            p.save()
            if available_deliveries.exists():
                random_delivery = random.choice(list(available_deliveries))

                Deliveryupdate.objects.create(
                    date=date.today(),
                    master_id=b,          # booking object
                    delivery=random_delivery,
                    type="custom",
                    status="assigned"
                )
            return HttpResponse("<script>alert('Payment Sucessfull');window.location='/core/cust_smoothie';</script>")
        return render (request, "payment.html",{"t":total_amount,"delivery":delivery})
    
def seller_booking_pie_chart(request):
    seller_data = ( Cart.objects.values('smoothie__name')
        .annotate(booking_count=Count('master_id', distinct=True))
            .order_by('-booking_count'))
    labels = [item['smoothie__name'] for item in seller_data if
    item['smoothie__name']]
    data = [item['booking_count'] for item in seller_data if
    item['smoothie__name']]
    context = {
    'labels': labels,
    'data': data,
    }
    return render(request, 'reports.html', context)

def remove_cart(request):
    if request.method == "POST":
        data = json.loads(request.body)

        cart_item = Cart.objects.get(
            id=data['cart_id'],
            customer=request.user
        )

        cart_item.delete()

        return JsonResponse({"status": "success"})
    

def update_custom_quantity(request):
    if request.method == "POST":
        data = json.loads(request.body)

        try:
            item = CustomIngredients.objects.get(
                id=data['item_id'],
                customer=request.user
            )

            item.quantity = int(data['quantity'])
            item.price = item.ingredients.price * item.quantity/100
            item.save()

            return JsonResponse({
                "status": "success",
                "item_total": item.price
            })

        except CustomIngredients.DoesNotExist:
            return JsonResponse({"status": "error"})
        
def remove_ccart(request):
    if request.method == "POST":
        data = json.loads(request.body)

        try:
            item = CustomIngredients.objects.get(
                id=data['cart_id'],
                customer=request.user
            )
            item.delete()
            return JsonResponse({"status": "success"})
        except CustomIngredients.DoesNotExist:
            return JsonResponse({"status": "error"})
        
def smoothie_detail(request, id):
    smoothie = Smoothie.objects.get(id=id)
    reviews = smoothie.reviews.all()

    if request.method == "POST":
        rating = int(request.POST.get("rating"))
        comment = request.POST.get("comment")

        Review.objects.update_or_create(
            smoothie=smoothie,
            customer=request.user,
            defaults={
                "rating": rating,
                "comment": comment
            }
        )

    average_rating = reviews.aggregate(
        Avg('rating')
    )['rating__avg']

    return render(request, "smoothie_details.html", {
        "s": smoothie,
        "reviews": reviews,
        "average_rating": average_rating
    })
    
# def rate_smoothie(request):
#     if request.method == "POST":
#         data = 
#         smoothie = Smoothie.objects.get(id=data['smoothie_id'])

#         Rating.objects.update_or_create(
#             user=request.user,
#             smoothie=smoothie,
#             defaults={'value': data['rating']}
#         )

#         return JsonResponse({'status': 'success'})



    


# def payment(request):
#     dat=date.today()
#     if request.method=="POST":
#         amount=request.POST.get("total")
#         # id=request.POST.get("id")
#         b=Booking()
#         b.customer=request.user
#         b.date=date
#         b.amount=amount
#         b.status="sucessfull"
#         b.save()
#         return HttpResponse("<script>alert('added to fav');window.location='/core/cust_smoothie';</script>")
#     else:
#         c=Customer.objects.get(user=request.user)
#         return render (request, "payment.html",{"c":c,"d":dat})

# def payment(request,no):
#     if request.method=="POST":
#         smoothie=request.POST.getlist("smoothie[]")
#         amount=request.POST.get("price")

#         b=Booking()
#         b.customer=request.user
#         b.date=date.today()
#         b.amount=request.POST.get("amount")
#         b.save()
#         for i in smoothie:
#             b.smoothie.add(i)
#         return HttpResponse("<script>alert('Insertion sucessfull');window.location='/core/smoothie';</script>")
#     else:
#         c=Customer.objects.filter(id=no)
#         return render (request, "payment.html",{"c":c})


    
from django.shortcuts import render
from .embedding_engine import recommend_smoothies

def suggestion(request):
    recommendations = None

    if request.method == "POST":
        user_query = request.POST.get("query")
        recommendations = recommend_smoothies(user_query)
        print(recommendations)

    return render(request, "suggestion.html", {"recommendations": recommendations})





    
from django.db import models
from app_dashboard.models import Customer
from count_your_calories.users.models import User

# Create your models here.
class District(models.Model):
    name=models.CharField()

class Location(models.Model):
    name=models.CharField()
    district=models.ForeignKey(District,on_delete=models.CASCADE)

class Category(models.Model):
    name=models.CharField()
    desc=models.CharField()
    img=models.ImageField(upload_to="media/",null=True)

class Ingredients(models.Model):
    name=models.CharField()
    availability=models.CharField()
    simg=models.ImageField(upload_to="smoothie/",null=True) 
    price=models.IntegerField(default="100")
    calorie=models.IntegerField(default="100")

class Smoothie(models.Model):
    name=models.CharField()
    ingredients=models.ManyToManyField(Ingredients)
    availability=models.CharField()
    simg=models.ImageField(upload_to="smoothie/",null=True) 
    price=models.IntegerField(default="100")

class CustomSmoothie(models.Model):
    name=models.CharField()
    Customer=models.ForeignKey(User,on_delete=models.CASCADE)
    ingredients=models.ManyToManyField(Ingredients) 
    price=models.IntegerField(default="100")

class CustomIngredients(models.Model):
    Customer=models.ForeignKey(User,on_delete=models.CASCADE,related_name="cust")
    ingredients=models.ForeignKey(Ingredients,on_delete=models.CASCADE,related_name="ing")
    quantity=models.IntegerField()
    price=models.IntegerField()

class Delivery(models.Model):
    licence_no=models.CharField()
    contact=models.CharField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    status_choices=[("accept","accept"),("reject","reject"),("processing","processing")]
    status=models.CharField(("Enter role"),choices=status_choices,null=False,blank=False,default="processing")

class Booking(models.Model):
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    smoothie=models.ManyToManyField(Smoothie)
    date=models.DateField()
    amount=models.CharField()
    status=models.CharField()
    
class Cart(models.Model):
    customer=models.ForeignKey(User,on_delete=models.CASCADE,related_name="cart_user")
    smoothie=models.ForeignKey(Smoothie,on_delete=models.CASCADE,related_name="smoothie")
    quantity=models.CharField()
    amount= models.DecimalField(max_digits=10, decimal_places=2,default=0)

class Favourite(models.Model):
    customer=models.ForeignKey(User,on_delete=models.CASCADE,related_name="f_user")
    smoothie=models.ForeignKey(Smoothie,on_delete=models.CASCADE,related_name="f_smoothie")
    
    







    
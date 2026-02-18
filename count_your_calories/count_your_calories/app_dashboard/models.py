from django.db import models

from count_your_calories.users.models import User

# Create your models here.
class Customer(models.Model):
    address=models.CharField()
    location=models.CharField()
    contact=models.CharField()
    age=models.CharField()
    height=models.CharField()
    weight=models.CharField()
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=1)


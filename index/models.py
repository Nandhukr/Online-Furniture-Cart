from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#mobiles
class Furniture(models.Model):
    CATEGORY=(
        ('tables','tables'),
        ('desks','desks'),
        ('cabinets','cabinets'),
        ('beds','beds'),
        ('chairs and seating','chairs and seating'),
    )
    name=models.CharField(max_length=100)
    brand=models.CharField(max_length=100)
    category=models.CharField(max_length=100,choices=CATEGORY)
    price=models.CharField(max_length=100)
    description=models.TextField(max_length=1000)
    weight=models.CharField(max_length=100)
    photo1=models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name
    
#cart
class Cart(models.Model):
    user=models.ForeignKey(User,models.CASCADE)
    product=models.ForeignKey(Furniture,models.CASCADE)

    
    

#order
class Order(models.Model):
    user=models.ForeignKey(User,models.CASCADE)
    product=models.ForeignKey(Furniture,models.CASCADE)
    price=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    mobile_no=models.CharField(max_length=10)
    pincode=models.CharField(max_length=6)
    house=models.CharField(max_length=100)
    street=models.CharField(max_length=100)
    landmark=models.CharField(max_length=100)
    town=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now=False)
    




    
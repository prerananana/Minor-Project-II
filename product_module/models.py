# from importlib.resources import Package as auth_Package
from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser

# Create your models here.
# class User_Role(AbstractUser):
#     is_admin= models.BooleanField('Is admin', default=False)
#     is_customer = models.BooleanField('Is customer', default=False)
#     is_agency = models.BooleanField('Is agency', default=False)

class Customer(models.Model):
    customer_id= models.IntegerField()
    fullname= models.CharField(max_length=200)
    address= models.CharField(max_length=200)
    phone= models.CharField(max_length=200)
    email= models.CharField(max_length=300)

class Guide(models.Model):
    guide_id= models.IntegerField()
    guide_name= models.CharField(max_length=200)
    experience= models.IntegerField()
    type= models.CharField(max_length=100)
    contact_no= models.CharField(max_length=200)
    no_of_routes= models.IntegerField()
    review= models.CharField(max_length=500)

class Package(models.Model):
    package_id= models.IntegerField()
    package_name= models.CharField(max_length=200)
    price= models.FloatField()
    type= models.CharField(max_length=100)
    image_url= models.CharField(max_length=500, default="")
    def image_tag(self):
        return mark_safe(f'<img src="{self.image_url}" width="50" height="50" />')
    time= models.CharField(max_length=100, default="5 days")
    package_name_alias= models.CharField(max_length=100, default="")

class Agency(models.Model):
    agency_id= models.IntegerField()
    agency_name= models.CharField(max_length=200)
    location= models.CharField(max_length=200)
    package= models.ForeignKey(Package, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Agencies"

class Booking(models.Model):
    booking_id= models.IntegerField()
    destination= models.CharField(max_length=200)
    ticket_type= models.CharField(max_length=200)
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    guide= models.ForeignKey(Guide, on_delete=models.CASCADE)
    package= models.ForeignKey(Package, on_delete=models.CASCADE)
    # destination_detail= models.ForeignKey(destination_detail, on_delete=models.CASCADE)

class destination_detail(models.Model):
    destination_id= models.IntegerField()
    destination= models.CharField(max_length=200)
    description= models.TextField(blank= True)
    days= models.TextField(blank=True, default="")
    package= models.ForeignKey(Package, on_delete=models.CASCADE)

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    entered_on = models.DateTimeField()
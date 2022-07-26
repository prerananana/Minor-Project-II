from django.db import models
from django.utils.html import mark_safe

# Create your models here.
class customerDetails(models.Model):
    
    fullname= models.CharField(max_length=200)
    username= models.CharField(max_length=200, default="")
    password= models.CharField(max_length=200, default="")
    address= models.CharField(max_length=200)
    phone= models.CharField(max_length=200)
    email= models.CharField(max_length=300)

class guide(models.Model):
    guide_id= models.IntegerField()
    guide_name= models.CharField(max_length=200)
    experience= models.IntegerField()
    type= models.CharField(max_length=100)
    contact_no= models.CharField(max_length=200)
    no_of_routes= models.IntegerField()
    review= models.CharField(max_length=500)

class package(models.Model):
    package_id= models.IntegerField()
    package_name= models.CharField(max_length=200)
    price= models.FloatField()
    type= models.CharField(max_length=100)
    image_url= models.CharField(max_length=500, default="")
    def image_tag(self):
        return mark_safe(f'<img src="{self.image_url}" width="50" height="50" />')

class agency(models.Model):
    agency_id= models.IntegerField()
    agency_name= models.CharField(max_length=200)
    location= models.CharField(max_length=200)
    package= models.ForeignKey(package, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Agencies"

class booking(models.Model):
    booking_id= models.IntegerField()
    destination= models.CharField(max_length=200)
    ticket_type= models.CharField(max_length=200)
    
    guide= models.ForeignKey(guide, on_delete=models.CASCADE)
    package= models.ForeignKey(package, on_delete=models.CASCADE)
class contactDetails(models.Model):
    message=models.TextField(max_length=500, default="")
    name= models.CharField(max_length=200)
    email= models.CharField(max_length=200,  default="")
    subject = models.CharField(max_length=200, default="")






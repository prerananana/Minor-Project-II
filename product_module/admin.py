from importlib.resources import Package
from pyexpat import model
from django.contrib import admin
from .models import guide, customerDetails, package, agency, booking,contactDetails

class guideAdmin(admin.ModelAdmin):
    list_display= ["guide_name", "experience", "type", "contact_no", "review",]
    search_fields= ["guide_id", "guide_name", "experience", "type", "contact_no", "review",]
    list_filter= ["guide_name", "experience", "type", "contact_no", "review", ]
    class Meta:
        model= guide
admin.site.register(guide, guideAdmin)

class customerAdmin(admin.ModelAdmin):
    list_display= ["fullname","username","password", "address", "phone", "email",]
    search_fields= ["fullname","username","password", "address", "phone", "email",]
    list_filter= ["fullname","username","password", "address", "phone", "email",]
    class Meta:
        model= customerDetails
admin.site.register(customerDetails, customerAdmin)

class packageAdmin(admin.ModelAdmin):
    list_display= ["package_id", "package_name", "price", "type", ]
    search_fields= ["package_id", "package_name", "price", "type", ]
    list_filter= ["package_name", "price", "type", ]
    class Meta:
        model= Package
        verbose_name_plural= "Packages"
admin.site.register(package, packageAdmin)

class agencyAdmin(admin.ModelAdmin):
    list_display= [ "agency_name", "location", "package_id",]
    search_fields= [ "agency_name", "location", "package_id",]
    list_filter= [ "agency_name", "location", "package_id",]
    class Meta:
        model= agency
admin.site.register(agency, agencyAdmin)

class bookingAdmin(admin.ModelAdmin):
    list_display= ["destination", "ticket_type", "guide", "package",]
    search_fields= ["booking_id", "destination", "ticket_type",  "guide", "package",]
    list_filter= ["booking_id","destination", "ticket_type",  "guide", "package",]
    class Meta:
        model= booking
admin.site.register(booking, bookingAdmin)
class contactAdmin(admin.ModelAdmin):
    list_display= ["message","name", "email", "subject",]
    search_fields= ["message","name", "email", "subject",]
    list_filter= ["message","name", "email", "subject",]
    class Meta:
        model= contactDetails
admin.site.register(contactDetails, contactAdmin)


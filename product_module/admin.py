from importlib.resources import Package
from pyexpat import model
from django.contrib import admin
from .models import Guide, Customer, Package, Agency, Booking, destination_detail

class guideAdmin(admin.ModelAdmin):
    list_display= ["guide_name", "experience", "type", "contact_no", "review",]
    search_fields= ["guide_id", "guide_name", "experience", "type", "contact_no", "review",]
    list_filter= ["guide_name", "experience", "type", "contact_no", "review", ]
    class Meta:
        model= Guide
admin.site.register(Guide, guideAdmin)

class customerAdmin(admin.ModelAdmin):
    list_display= ["fullname", "address", "phone", "email",]
    search_fields= ["customer_id", "fullname", "address", "phone", "email",]
    list_filter= ["customer_id", "fullname", "address", "phone", "email", ]
    class Meta:
        model= Customer
admin.site.register(Customer, customerAdmin)

class packageAdmin(admin.ModelAdmin):
    list_display= ["package_id", "package_name", "price", "type", "package_name_alias"]
    search_fields= ["package_id", "package_name", "price", "type", ]
    list_filter= ["package_name", "price", "type", ]
    class Meta:
        model= Package
        verbose_name_plural= "Packages"
admin.site.register(Package, packageAdmin)

class agencyAdmin(admin.ModelAdmin):
    list_display= ["agency_id", "agency_name", "location", "package_id",]
    search_fields= ["agency_id", "agency_name", "location", "package_id",]
    list_filter= ["agency_id", "agency_name", "location", "package_id",]
    class Meta:
        model= Agency
admin.site.register(Agency, agencyAdmin)

class bookingAdmin(admin.ModelAdmin):
    list_display= ["destination", "ticket_type", "customer", "guide", "package",]
    search_fields= ["booking_id", "destination", "ticket_type", "customer", "guide", "package",]
    list_filter= ["booking_id","destination", "ticket_type", "customer", "guide", "package",]
    class Meta:
        model= Booking
admin.site.register(Booking, bookingAdmin)

class destination_detailAdmin(admin.ModelAdmin):
    list_display= ["destination_id", "destination", "description","days", "package",]
    search_fields= ["destination_id", "destination", "description","package",]
    list_filter= ["destination_id", "destination", "description","package",]
    class Meta:
        model= destination_detail
admin.site.register(destination_detail, destination_detailAdmin)

from .models import CartItem
admin.site.register(CartItem)


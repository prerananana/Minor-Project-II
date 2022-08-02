from .models import PaymentGateway, Invoice, InvoiceDetail
from django.contrib import admin
# from product_module.models import CartItem

# admin.site.register(CartItem)

class PaymentGatewayAdmin(admin.ModelAdmin):
    list_display = ["token", "balance", "expiry_date", "is_active",]
class Meta:
    model = PaymentGateway
admin.site.register(PaymentGateway, PaymentGatewayAdmin)

admin.site.register(Invoice)
admin.site.register(InvoiceDetail)
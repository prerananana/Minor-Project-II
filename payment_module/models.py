from django.db import models
import uuid
from django.contrib.auth.models import User
from product_module.models import Package


# Create your models here.
class PaymentGateway(models.Model):
    token = models.UUIDField(default= uuid.uuid4,editable=False)
    expiry_date = models.DateField()
    balance = models.FloatField()
    is_active = models.BooleanField()

class Invoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.UUIDField()
    payment_date = models.DateTimeField()
    total_amount = models.FloatField()

    def __str__(self) -> str:
        return self.total_amount

class InvoiceDetail(models.Model):
    invoice = models.ForeignKey("Invoice", on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, default=1)
    quantity = models.IntegerField()
    sub_amount = models.FloatField()
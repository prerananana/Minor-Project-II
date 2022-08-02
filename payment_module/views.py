from django.shortcuts import render, redirect
from .models import PaymentGateway, Invoice, InvoiceDetail
from product_module.models import CartItem, Package
from datetime import date, datetime
from django.db import transaction
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="/admin/login")
def cart(request):
    # global package
    # get request data
    package_id = request.GET.get("id")
    quantity = request.GET.get("qty")
    if package_id:
    # retrieve product data
        package = Package.objects.get(id=package_id)
        try:
            # get cart item and increase quantity
            cart_item = CartItem.objects.get(user=request.user, package=package)
            cart_item.quantity += int(quantity)
            cart_item.entered_on = datetime.now()
        except CartItem.DoesNotExist:
            # initialize cart item
            cart_item = CartItem(
                user=request.user,
                package=package,
                quantity=int(quantity),
                entered_on = datetime.now(),
            )
            # save to database
        cart_item.save()
        cart_items = CartItem.objects.filter(user=request.user)
        total = 0
        for item in cart_items:
            total += item.package.price * item.quantity
            # return view
            context = {
                'cart_items': cart_items,
                'total': total,
            }
            return render(request, "cart.html", context)

def removecart(request, id):
    # global package
    try:
        # get cart item and increase quantity
        package = Package.objects.get(id=id)
        cart_item = CartItem.objects.get(user=request.user, package=package)
        cart_item.delete()
    except CartItem.DoesNotExist:
        pass
    # redirect to cart
    return redirect(cart)

def success_page(request):
    # global package
    message = request.session["message"]
    return render(request, "success_page.html", {"message": message})

def error_page(request):
    # global package
    message = request.session["message"]
    return render(request, "error.html", {"message": message})

def confirmpayment(request):
    # global package
    if request.method == "POST":
        token = request.POST.get("token")
        amount = request.POST.get("amount")
        # clean up
        token = token.strip()
        amount = float(amount)
        try:
            with transaction.atomic():
                 # open an atomic transaction, i.e. all successful or none
                make_payment(token, amount)
                maintain_invoice(request, token, amount)
        except Exception as e:
            request.session["message"] = str(e)
            return redirect(reverse('error_page'))
        else:
            request.session["message"] = f"Payment successfully completed with NRs. {amount} from your balance!"
            return redirect(reverse('success_page'))
def make_payment(token, amount):
    # global package
    try:
        payment_gateway = PaymentGateway.objects.get(token=token)
    except:
        raise Exception(f"Invalid token '{token}'")
 
    # Check if available amount is sufficient for payment
    if payment_gateway.balance < amount:
        raise Exception("Insufficient balance")
    # check for expiry date
    if payment_gateway.expiry_date < date.today():
        raise Exception("Token has expired")
    # deduct amount and save
    payment_gateway.balance -= amount
    payment_gateway.save()
def maintain_invoice(request, token, amount):
    # global package
    # retrieve cart items
    cart_items = CartItem.objects.filter(user=request.user)
    # save invoice
    invoice = Invoice(
        user = request.user,
        token = token,
        total_amount = amount,
        payment_date = datetime.now()
    )
    invoice.save()
    # save invoice detail
    for cart_item in cart_items:
        invoice_detail = InvoiceDetail(
        invoice = invoice,
        package = cart_item.package,
        quantity = cart_item.quantity,
        sub_amount = cart_item.quantity * cart_item.package.price
    )
    invoice_detail.save()
 
    # adjust product quantity and clear cart
    for cart_item in cart_items:
        # reduce quantity from Product
        package = Package.objects.get(id=cart_item.package.id)
        package.save()
            # clear cart for the user
        cart_item.delete()

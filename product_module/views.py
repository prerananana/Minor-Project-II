
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.db.models import Q
from .models import booking, package, guide, contactDetails,customerDetails,agency,package
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.

def AddContact(request):

    message = request.POST["me"]
    name = request.POST["name"]
    email = request.POST["e"]

    subject = request.POST["subject"]
    print("success")
    Contact_Info = contactDetails(message=message,name = name,email = email,subject=subject  )
    Contact_Info.save()
    return render(request, 'contact.html' ,{})

def NewUser(request):
    f_name=request.POST["full_name"]
    u_name=request.POST["user_name"]
    password=request.POST["pass"]
    address=request.POST["address"]
    phone=request.POST["phone"]
    email=request.POST["email"]

    Customer_Info = customerDetails(fullname = f_name,username = u_name,password = password, address = address,phone = phone, email = email,  )
    Customer_Info.save()
    return render(request, 'index.html' ,{})
    
def NewAgency(request,id):
    f_name=request.POST["agency_name"]
    location=request.POST["location"]
   
    query = package.objects.get(pk=id) 
    query.package.add(request.user)   
    Agency_Info = agency(agency_name = f_name,location = location,  )
    Agency_Info.save()
    return render(request, 'index.html' ,{})

def LogUser(request):
    if request.method == 'POST':
        username=request.POST["user_name"]
        password=request.POST["password"]

        Customer_Info = auth.authenticate(username=username,password=password)
        package = package.objects.get(id=id)
        if Customer_Info is not None:
            auth.login(request,Customer_Info)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login.html')
    else:
        return render(request, 'login.html' ,{})
def about(request):
    return render(request, 'about.html', {})

def packages(request):
    return render(request, 'packages.html', {})

def destination(request):
    destination= booking.objects.all()
    packages= package.objects.all()
    context = {'destination': destination,
              'packages': packages,
            }
    return render(request, 'travel_destination.html', context)

def blog(request):
    return render(request, 'blog.html', {})

def singleblog(request):
    return render(request, 'single-blog.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def destination_details(request):
    return render(request, 'destination_details.html', {})

def elements(request):
    return render(request, 'elements.html', {})

def Login(request):
    return render(request, 'login.html', {})

def Registration(request):
    return render(request, 'registration.html', {})

def Registration_agency(request):
    return render(request, 'registration_agency.html', {})
    
def Registration_guide(request):
    return render(request, 'registration_guide.html', {})

#info-needed
def index(request):
    if request.method == "GET":
        package_id = request.GET.get("package")
        guide_id = request.GET.get("guide")
        if package_id:
            filter_query = Q(package__id=package_id)
            bookings = booking.objects.filter(filter_query)
        elif guide_id:
            filter_query = Q(guide__id=guide_id)
            bookings = booking.objects.filter(filter_query)
        else:

    #         # new product : product that are registered since last 7 days (top 10 products)
    #         new_products = Product.objects.filter(Q(registered_on__gte=(datetime.now() - timedelta(days=7))))[:10]
            
            #info----needed-----
            bookings = booking.objects.all()
            packages = package.objects.all()
            guides = guide.objects.all()
            context = {
                'bookings': bookings,
                'packages': packages,
                'guides': guides,
                'search_query': '',
                }
            return render(request, 'index.html', context)

            #till----here-----
    # elif request.method == "POST":
    #     q = request.POST.get("query")
    # if "-" in q: 
    #     price_values = q.split("-")
    #     filter_query = Q(price__gte=price_values[0]) & Q(price__lte=price_values[1])
    # else:
    #     filter_query = Q(name__icontains=q) | Q(price__icontains=q) | Q(brand__name__icontains=q)
    #     products = Product.objects.filter(filter_query)
    #     new_products = Product.objects.filter(Q(registered_on__gte=(datetime.now() - timedelta(days=7))))[:10]
    #     categories = Category.objects.all()
    #     brands = Brand.objects.all()
    #     context = {
    #         'products': products,
    #         'new_products': new_products,
    #         'top_selling_products': new_products,  # TODO: get from invoicedetails later
    #         'categories': categories,
    #         'brands': brands,
    #         'search_query': q,
    #     }
    # return render(request, 'index.html', context)




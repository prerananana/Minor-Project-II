#from msilib.schema import Class
from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpResponseRedirect
from django.db.models import Q
from .models import booking, package, guide, destination_detail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
# Create your views here.


def about(request):
    bookings = booking.objects.all()
    packages = package.objects.all()
    guides = guide.objects.all()
    context = {
        'bookings': bookings,
        'packages': packages,
        'guides': guides,
    }
    return render(request, 'about.html', context)

def mardi(request):
    bookings = booking.objects.all()
    packages = package.objects.all()
    guides = guide.objects.all()
    context = {
        'bookings': bookings,
        'packages': packages,
        'guides': guides,
    }
    return render(request, 'mardi.html', context)

def mustang(request):
    bookings = booking.objects.all()
    packages = package.objects.all()
    guides = guide.objects.all()
    context = {
        'bookings': bookings,
        'packages': packages,
        'guides': guides,
    }
    return render(request, 'mustang.html', context)

def mountain(request):
    bookings = booking.objects.all()
    packages = package.objects.all()
    guides = guide.objects.all()
    context = {
        'bookings': bookings,
        'packages': packages,
        'guides': guides,
    }
    return render(request, 'mountain.html', context)

def langtang(request):
    bookings = booking.objects.all()
    packages = package.objects.all()
    guides = guide.objects.all()
    context = {
        'bookings': bookings,
        'packages': packages,
        'guides': guides,
    }
    return render(request, 'langtang.html', context)

def pokhara(request):
    bookings = booking.objects.all()
    packages = package.objects.all()
    guides = guide.objects.all()
    context = {
        'bookings': bookings,
        'packages': packages,
        'guides': guides,
    }
    return render(request, 'pokhara.html', context)

def annapurna(request):
    bookings = booking.objects.all()
    packages = package.objects.all()
    guides = guide.objects.all()
    context = {
        'bookings': bookings,
        'packages': packages,
        'guides': guides,
    }
    return render(request, 'annapurna.html', context)

def lumbini(request):
    bookings = booking.objects.all()
    packages = package.objects.all()
    guides = guide.objects.all()
    context = {
        'bookings': bookings,
        'packages': packages,
        'guides': guides,
    }
    return render(request, 'lumbini.html', context)

def chitwan(request):
    bookings = booking.objects.all()
    packages = package.objects.all()
    guides = guide.objects.all()
    context = {
        'bookings': bookings,
        'packages': packages,
        'guides': guides,
    }
    return render(request, 'chitwan.html', context)

def bhaktapur(request):
    bookings = booking.objects.all()
    packages = package.objects.all()
    guides = guide.objects.all()
    context = {
        'bookings': bookings,
        'packages': packages,
        'guides': guides,
    }
    return render(request, 'bhaktapur.html', context)

def rara(request):
    bookings = booking.objects.all()
    packages = package.objects.all()
    guides = guide.objects.all()
    context = {
        'bookings': bookings,
        'packages': packages,
        'guides': guides,
    }
    return render(request, 'rara.html', context)

def test(request):
    destination= destination_detail.objects.all()
    packages= package.objects.all()
    context= {
        'destination' : destination,
        'packages' : packages
    }
    return render(request, 'test.html', context)

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

def destination_detaill(request):
    # if request.method == "GET":
    #     destination_id = request.GET.get("destination")
    #     destination_details= destination_detail.objects.get(destination_id = destination_id)
    destination= destination_detail.objects.all()
    packages= package.objects.all()
    context= {
        'destination' : destination,
        'packages' : packages
    }
    return render(request, 'destination_details.html', context)

def elements(request):
    return render(request, 'elements.html', {})
def login(request):
    if request.method == 'POST':
        username= request.POST.get('user_name')
        password= request.POST.get('pass1')

        user= authenticate(username= username, password= password)

        if user is None:
            auth_login(request, user)
            fname= user.first_name
            return render(request, 'index.html', {'fname': fname} )
        
        else:
            messages.error(request, "Bad Credentials!")
            return redirect('index.html')
    return render(request, 'login.html', {})
def registration(request):
    if request.method == 'POST':
        fname= request.POST.get('fname')
        lname= request.POST.get('lname')
        username= request.POST.get('user_name')
        password= request.POST.get('pass1')
        confirm= request.POST.get('pass2')
        address= request.POST.get('address')
        phone= request.POST.get('phone')
        email= request.POST.get('email')

        myuser= User.objects.create_user(username, email, password)
        myuser.first_name= fname
        myuser.last_name= lname

        myuser.save()

        messages.success(request, "Your account has been sucessfully created!")
        return redirect('login.html')
    return render(request, 'registration.html', {})
def signout(request):
    logout(request)
    messages.success(request, "Logged Out Sucessfully")
    return redirect('index.html')
def submit(request):
    bookings = booking.objects.all()
    packages = package.objects.all()
    guides = guide.objects.all()
    context = {
        'bookings': bookings,
        'packages': packages,
        'guides': guides,
    }
    return render(request, 'submit_demo.html', context)
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




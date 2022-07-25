from django.urls import path

<<<<<<< HEAD
from .views import index,about,destination,blog,singleblog,contact,destination_details,elements, packages, login, registration
=======

from .views import index,about,destination,blog,singleblog,contact,destination_details,elements, packages,Login
>>>>>>> 1a79913892e2ec054656cf7385e9323856e4339d

urlpatterns = [
    path('', index),
    path('index.html', index),
    path('about.html', about),
    path('packages.html', packages),
    path('travel_destination.html', destination),
    path('blog.html',blog),
    path('single-blog.html',singleblog),
    path('contact.html',contact),
    path('destination_details.html',destination_details),
    path('elements.html',elements),
<<<<<<< HEAD
    path('login.html',login),
    path('registration.html',registration)
=======
    path('login.html',Login)
>>>>>>> 1a79913892e2ec054656cf7385e9323856e4339d
]
from django.urls import path
<<<<<<< HEAD
from .views import index,about,destination,blog,singleblog,packages
=======
from .views import index,about,destination,blog,singleblog,contact,destination_details,elements
>>>>>>> c36e4b68b47eacd58414f5d2d75cc36e4c00a16a
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
    path('elements.html',elements)
]
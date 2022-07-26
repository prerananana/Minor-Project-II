from django.urls import path

from product_module import views

from .views import index,about,destination,blog,singleblog,contact,destination_details,elements, packages,Login,Registration

urlpatterns = [
    path('', index),
    path('index.html', index),
    path('about.html', about),
    path('packages.html', packages),
    path('travel_destination.html',destination),
    path('blog.html',blog),
    path('single-blog.html',singleblog),
    path('contact.html',contact),
    path('destination_details.html',destination_details),
    path('elements.html',elements),
    path('login.html',Login),
    path('registration.html',Registration),
    path('add_contact', views.AddContact, name='add_contact')
    path('new_user', views.NewUser, name='new_user')
   
]
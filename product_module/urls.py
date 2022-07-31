from django.urls import path
from product_module import views

from .views import index,about,destination,blog,singleblog,contact,destination_details,elements, packages,Login,Registration,Registration_agency,Registration_guide

urlpatterns = [
    path('', index),
    path('index.html', index),
    path('about.html', about),
    path('packages.html', packages),
    path('travel_destination.html', destination),
    path('blog.html',blog),
    path('single-blog.html',singleblog),
    path('contact.html',contact),
    path('registration.html',Registration),
    path('registration_agency.html',Registration_agency),
    path('registration_guide.html',Registration_guide),
    path('destination_details.html',destination_details),
    path('elements.html',elements),
    path('login.html',Login),
    path('add_contact', views.AddContact, name='add_contact'),
    path('new_user', views.NewUser, name='new_user'),
    path('new_agency', views.NewAgency, name='new_agency'),

    path('log_user', views.LogUser, name='log_user')
]
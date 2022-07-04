from django.urls import path
from .views import index,about,destination,blog,singleblog,packages
urlpatterns = [
    path('', index),
    path('index.html', index),
    path('about.html', about),
    path('packages.html', packages),
    path('travel_destination.html', destination),
    path('blog.html',blog),
    path('single-blog.html',singleblog)
]
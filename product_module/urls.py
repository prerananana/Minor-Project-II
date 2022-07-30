from django.urls import path

from .views import index,about,destination,blog,singleblog,contact,destination_detaill,elements, packages, login, registration, test, rara, mardi, mustang, langtang, mountain, lumbini, chitwan, pokhara, bhaktapur, annapurna, submit, signout

urlpatterns = [
    path('', index),
    path('index.html', index),
    path('about.html', about),
    path('packages.html', packages),
    path('travel_destination.html', destination),
    path('blog.html',blog),
    path('single-blog.html',singleblog),
    path('contact.html',contact),
    path('destination_details.html',destination_detaill),
    path('elements.html',elements),
    path('login.html',login),
    path('signout.html',signout),
    path('registration.html',registration),
    path('test.html',test),
    path('rara.html',rara),
    path('mardi.html',mardi),
    path('mustang.html',mustang),
    path('mountain.html',mountain),
    path('langtang.html',langtang),
    path('pokhara.html',pokhara),
    path('annapurna.html',annapurna),
    path('lumbini.html',lumbini),
    path('chitwan.html',chitwan),
    path('bhaktapur.html',bhaktapur),
    path('submit_demo.html',submit)
]
from django.conf.urls import url
from django.urls import path, re_path, include
from AppTwo import views

urlpatterns = [
   path('', views.index, name='index'), 
   path('users.html', views.users, name='users')
   path('help.html', views.help, name='help'), 
   path('contact.html', views.contact, name='contact'), 
]


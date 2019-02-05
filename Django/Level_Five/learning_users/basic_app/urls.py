from django.urls import path
from basic_app import views

# TEMPLATE URLS! 
app_name = 'basic_app'

urlpatterns=[
	path('',views.register,name='register'),

]

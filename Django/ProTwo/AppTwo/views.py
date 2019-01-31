from django.shortcuts import render
from django.http import HttpResponse 
from AppTwo.models import Topic,Webpage,AccessRecord,User 

# Create your views here.
def index(request): 
	webpages_list = AccessRecord.objects.order_by('date')
	date_dict = {'access_records':webpages_list}
	# my_dict = {'insert_me':"Now i'm coming from AppTwo/index.html!"}
	return render(request, 'AppTwo/index.html', context=date_dict)

def users(request):
	
	# user_list = User.objects.order_by('first_name')
	# user_dict = {'users':user_list}
	# return render(request,'AppTwo/users.html',context=user_dict)

def help(request): 
	helpdict = {'help_insert': "HELP PAGE"}
	return render(request, 'AppTwo/help.html', context=helpdict)

def contact(request): 
	contact_dict = { 'contact_insert': "Contact Us"}
	return render(request, 'AppTwo/contact.html', context=contact_dict)
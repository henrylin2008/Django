from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def index(request): 
	my_dict = {'insert_me':"Now i'm coming from AppTwo/index.html!"}
	return render(request, 'AppTwo/index.html', context=my_dict)

def help(request): 
	helpdict = {'help_insert': "HELP PAGE"}
	return render(request, 'AppTwo/help.html', context=helpdict)

def contact(request): 
	contact_dict = { 'contact_insert': "Contact Us"}
	return render(request, 'AppTwo/contact.html', context=contact_dict)
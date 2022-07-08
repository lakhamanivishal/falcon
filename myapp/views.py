from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
	return render(request,'index.html')

def about(request):
	return render(request,'about.html')

def contact(request):
	if request.method=="POST":
		Contact.objects.create(

				name=request.POST['name'],
				email=request.POST['email'],
				mobile=request.POST['mobile'],
				remarks=request.POST['remarks'],
				
		)

		msg="Contact Saved Sucessfully"
		return render(request,'contact.html',{'msg':msg})	
	else:
		return render(request,'contact.html')	

def portfolio(request):
	return render(request,'portfolio.html')

def signup(request):
	if request.method=="POST":
		user.objects.create(

				uname=request.POST['fname'],
				lname=request.POST['lname'],
				email=request.POST['email'],
				mobile=request.POST['mobile'],
				remarks=request.POST['remarks'],

				)
		return render(request,'signup.html')	

	else:
		return render(request,'signup.html')		
				
		



def login(request):
	return render(request,'login.html')


def falcon(request):
	return render(request,'falcon.html') 	

def rhinofact(request):
	return render(request,'rhinofact.html')

def butterfly(request):
	return render(request,'butterfly.html')	
	
def tiger(request):
	return render(request,'tiger.html')		

def vultures(request):
	return render(request,'vultures.html')		

def lion(request):
	return render(request,'lion.html')			

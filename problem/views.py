from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .models import *

def registerPage(request):
	form =CreateUserForm()

	if request.method=='POST':
		form =CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request,"Thanks for registering " + user)
			return redirect('login')


	context={'form':form}
	return render(request,'register.html',context)

def loginPage(request):
	
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request,user)
			return redirect('home')
		else:
			messages.success(request,"Invalid username or password")
	context={}

	return render(request,'login.html',context)

def logoutUser(request):
	logout(request)
	return redirect('login')


@login_required(login_url='/login/')
def HomeView(request):
	easys = easy.objects.all();
	mediums = medium.objects.all();
	hards = hard.objects.all();
	context = {'easys':easys,'mediums':mediums,'hards':hards}
	return render(request,'home.html',context)

@login_required(login_url='/login/')
def EasyView(request):
	easys = easy.objects.all();
	context = {'easys':easys}
	return render(request,'easy.html',context)

@login_required(login_url='/login/')
def MediumView(request):
	mediums = medium.objects.all();
	context = {'mediums':mediums}
	return render(request,'medium.html',context)

@login_required(login_url='/login/')
def HardView(request):
	hards = hard.objects.all();
	context = {'hards':hards}
	return render(request,'hard.html',context)
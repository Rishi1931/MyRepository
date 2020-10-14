from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

from django.contrib.auth.forms import UserCreationForm
from .forms import  CreateUserForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")

        else:
            messages.info(request, 'Invalid Credentials')
            return redirect("login")

    else:
        return render(request, 'login.html')

        


def register(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

		

			messages.success(request, 'Account was created for ' + username)

			return redirect('login')
		

	context = {'form':form}
	return render(request, 'register.html', context)



def logout(request):
    auth.logout(request)
    return redirect('/')


def profile(request):


	context = {}
	return render(request, 'profile.html', context)
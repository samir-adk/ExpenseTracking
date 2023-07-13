from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from authentication.forms import RegisterForm
from django.http import HttpResponseRedirect
# Create your views here.
def LoginView(request):
	if request.method=="POST":
		form=AuthenticationForm(request,data=request.POST)
		if form.is_valid():
			user_name=form.cleaned_data.get('username')
			password=form.cleaned_data.get('password')
			check_login=authenticate(request,username=user_name,password=password)
			if check_login is not None:
				login(request,check_login)
				return HttpResponseRedirect(reverse('expenses:index'))
	return render(request,'registration/login.html',{'form':AuthenticationForm()})

def RegisterView(request):
	User=get_user_model()
	if request.method=='POST':
		save_data=RegisterForm(request.POST)
		if save_data.is_valid():
			user=save_data.save()
			login(request,user)
			return HttpResponseRedirect(reverse('authentication:login'))
	return render(request,'registration/register.html',{'form':RegisterForm()})


def LogoutView(request):
	if request.method=='POST':
		logout(request)
		return HttpResponseRedirect(reverse('authentication:login'))
	return render(request,'registration/logout.html')
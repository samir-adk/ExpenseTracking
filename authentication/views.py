from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.
def LoginView(request):
	if request.method=="POST":
		print('post...........')
		form=AuthenticationForm(request,data=request.POST)
		if form.is_valid():
			print('...........vlid form')
			user_name=form.cleaned_data.get('username')
			password=form.cleaned_data.get('password')
			print(user_name)
			check_login=authenticate(request,username=user_name,password=password)
			if check_login is not None:
				print('yes authenticate')
				login(request,check_login)
				return HttpResponseRedirect(reverse('expenses:index'))
	return render(request,'registration/login.html',{'form':AuthenticationForm()})
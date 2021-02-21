from django.shortcuts import render, HttpResponse, redirect
from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .forms import LoginForm, RegForm
from django.urls import reverse

def home(request):
	return render(request, "home.html", {})

def login(request):
	if request.method == 'POST':
		login_form = LoginForm(request.POST)
		if login_form.is_valid():
			user = login_form.cleaned_data['user']
			auth.login(request, user)
			return redirect(request.GET.get('from', reverse('home')))
	else:
		login_form = LoginForm()

	context = {}
	context['login_form'] = login_form
	return render(request, 'login.html', context)

def register(request):
	if request.method == 'POST':
		reg_form = RegForm(request.POST)
		if reg_form.is_valid():
			username = reg_form.cleaned_data['username']
			email = reg_form.cleaned_data['email']
			password = reg_form.cleaned_data['password']
			user = User.objects.create_user(username, email, password)
			user.save()
			user = auth.authenticate(username=username, password=password)
			auth.login(request, user)
			return redirect(request.GET.get('from', reverse('home')))
	else:
		reg_form = RegForm()

	context = {}
	context['reg_form'] = reg_form
	return render(request, 'register.html', context)

def umanagement(request):
	return render(request, "umanagement.html", {})

def ulogout(request):
	logout(request)
	return redirect(request.GET.get('from', reverse('home')))
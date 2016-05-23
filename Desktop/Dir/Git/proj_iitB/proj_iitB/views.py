from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.template.loader import get_template
from django.template import Context
from django.views.generic.base import TemplateView
from django.core.context_processors import csrf
#from forms import RegistrationForm
from django.contrib.auth.forms import UserCreationForm
import requests

def login(request):
	log_content = {}
	log_content.update(csrf(request))
	return render_to_response('login.html', log_content)

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/accounts/loggedin')
	else:
		return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
	return render_to_response('loggedin.html', {'full_name': request.user.username})

def invalid_login(request):
	return render_to_response('invalid_login.html')

def logout(request):
	auth.logout(request)
	return render_to_response('logout.html')

def register_user(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save() # saves in database
			return HttpResponseRedirect('/accounts/register_success/')

	args = {}
	args.update(csrf(request))

	args['form'] = UserCreationForm()
	# print args
	return render_to_response('register.html', args)

def register_success(request):
	# print 'hello galaxy'
	return render_to_response('register_success.html')

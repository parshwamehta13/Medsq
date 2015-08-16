from django.shortcuts import render
from django.template import RequestContext, Context, Template, loader
from django.shortcuts import render_to_response, redirect
from django.http import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def login_auth(request):
	username = ''
	password = ''

	t = loader.get_template('login.html')
	c = RequestContext(request)
	if request.method == 'GET':
		return HttpResponse(t.render(c))	
	

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username = username, password = password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponse("Successfully logged in! :D")#HttpResponse("Succesfully logged in!! :D")
			else:
				return HttpResponse("This account has been deactivated.")
	return HttpResponse("Please enter a valid username and password")#return HttpResponse(t.render(c))
	
@login_required(login_url = '/login')

def logout(request):
	logout(request,user)
	HttpResponse('/main/')
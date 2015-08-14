from django.shortcuts import render
from django.template import RequestContext, Context, Template, loader
from django.shortcuts import render_to_response, redirect
from django.http import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def main(request):
	username = ''
	password = ''

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username = username, password = password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/main/')
		else:
			print("This account has been deactivated.")
		return HttpResponse("Please enter a valid username and password")
	
	t = loader.get_template('main_page.html')
	c = RequestContext(request)
	#if request.method == 'GET':
	return HttpResponse(t.render(c))	
	#return HttpResponse(t.render(c))
	#This is the place for the block of comment 
	
	
	#render_to_response('main_page.html', context_instance=RequestContext(request))'''
#@login_required(login_url = '/login/')

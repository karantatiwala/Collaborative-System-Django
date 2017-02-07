from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.contrib import auth

from django.contrib import sessions
from forms import Sign_Up_DataForm, LoginForm
from django.contrib import messages
from models import *

# Create your views here.


@csrf_protect
def signup(request):
	if request.POST:
		form = Sign_Up_DataForm(request.POST)
		username = request.POST.get('username', '')
		if form.is_valid():
			check = Sign_Up_Data.objects.filter(username=username).first()
			if check == None:
				
				form.save()
				request.session['username'] = username
				return HttpResponseRedirect('/login/after_login')
			else:
				messages.error(request, 'Username Already Taken')
				# return render(request, 'templates/signup.html', {'form' : form})
				return HttpResponseRedirect('/login/signup')
	else:
		form = Sign_Up_DataForm()

	# args = {}
	# args.update(csrf(request))

	# args['form'] = form

	return render(request, 'home.html')

# @csrf_protect
# def login(request):
# 	form1 = LoginForm(request.POST)
# 	args = {}
# 	# args.update(csrf(request))

# 	args['form1'] = form1
# 	return render(request, 'login.html', args)

@csrf_protect
def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	
	form = LoginForm(request.POST)
	user = Sign_Up_Data.objects.filter(username=username).first()

	# print password, user.password
	if user != None:
		if user.password == password:
			request.session['username'] = username
			return HttpResponseRedirect('/login/after_login')
			# return HttpResponseRedirect('/')
		else:
			messages.error(request, 'Invalid Credentials')
			return HttpResponseRedirect('/login/')

			# return HttpResponse("Invalid Credentials")
	else:
		messages.error(request, 'Plz signup first')
		return HttpResponseRedirect('/login/signup')


def after_login(request):
	if 'username' in request.session:
		print request.session['username']
		# return HttpResponse("yo yo bappa")
		username = request.session['username']

		return render_to_response('home.html', {'username' : username})
	else:
		return HttpResponse("404 not found")

def logout(request):
	del request.session['username']
	# print request.session['username']
	return HttpResponseRedirect('/')
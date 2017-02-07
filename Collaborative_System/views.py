from django.shortcuts import render_to_response, render
from login.forms import *
from django.contrib import sessions


def home(request):
	form = Sign_Up_DataForm
	form1 = LoginForm
	# print request.session['username']
	return render(request, 'home.html', {'form': form, 'form1':form1})

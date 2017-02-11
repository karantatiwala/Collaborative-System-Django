from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.contrib import auth

from django.contrib import sessions
from forms import Sign_Up_DataForm, LoginForm
from django.contrib import messages
from models import *
from upload_data.forms import DocumentForm

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from .models import Stock
from .serializers import Sign_Up_DataSerializer





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
		form2 = DocumentForm()

		return render(request, 'home.html', {'username' : username,'form2': form2})
	else:
		return HttpResponse("404 not found")

def logout(request):
	del request.session['username']
	# print request.session['username']
	return HttpResponseRedirect('/')


def Iyear(request):
	if 'username' in request.session:
		print request.session['username']
		username = request.session['username']
		return render(request, 'Ist_Year.html', {'username' : username})
	else:
		return HttpResponse("404 not found")

def IIyear(request):
	if 'username' in request.session:
		print request.session['username']
		username = request.session['username']
		return render(request, 'IInd_Year.html', {'username' : username})
	else:
		return HttpResponse("404 not found")

def IIIyear(request):
	if 'username' in request.session:
		print request.session['username']
		username = request.session['username']
		return render(request, 'IIIrd_Year.html', {'username' : username})
	else:
		return HttpResponse("404 not found")

def IVyear(request):
	if 'username' in request.session:
		print request.session['username']
		username = request.session['username']
		return render(request, 'IVth_Year.html', {'username' : username})
	else:
		return HttpResponse("404 not found")





# from django.shortcuts import get_object_or_404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# # from .models import Stock
# from .serializers import Sign_Up_DataSerializer



# List all Sign_Up_Data Or Create a new one
# Sign_Up_Data/
class Sign_Up_DataList(APIView):

	def get(self, request):
		signup = Sign_Up_Data.objects.all()
		serializer = Sign_Up_DataSerializer(signup, many=True)
		return Response(serializer.data)

	def post(self):
		pass
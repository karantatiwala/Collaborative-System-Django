from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from login.models import *
from models import Document
from forms import DocumentForm
from django.contrib import sessions
from django.core.mail import send_mail



def home(request):
	if 'username' in request.session:
		print request.session['username']
		username = request.session['username']

		documents = Document.objects.filter(username=username)
		# print documents
		return render(request, 'home.html', { 'documents': documents, 'username': request.session['username']})


# def simple_upload(request):
#     if request.method == 'POST' and request.FILES['myfile']:
#         myfile = request.FILES['myfile']
#         fs = FileSystemStorage()
#         filename = fs.save(myfile.name, myfile)
#         uploaded_file_url = fs.url(filename)
#         return render(request, 'simple_upload.html', {
#             'uploaded_file_url': uploaded_file_url
#         })
#     return render(request, 'simple_upload.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
			instance = form.save(commit=False)
			instance.username = request.session['username']
			# form.save()
			instance.save()
			username = request.session['username']
			check = Sign_Up_Data.objects.filter(username=username).first()
			print check.email
			# send_mail('Regarding your notes upload', 'We have recieved your query regarding the notes you have uploaded, we will back to you soon.', 'karantatiwala@gmail.com', [check.email])
			return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })
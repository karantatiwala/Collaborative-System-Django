from django import forms
from models import Sign_Up_Data


class Sign_Up_DataForm(forms.ModelForm):

	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = Sign_Up_Data
		fields = ('username', 'email', 'country', 'password')

class LoginForm(forms.ModelForm):

	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = Sign_Up_Data
		fields = ('username', 'password')


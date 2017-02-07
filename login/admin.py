from django.contrib import admin

# Register your models here.
from .models import Sign_Up_Data


class SignUp(admin.ModelAdmin):
	list_display = ('username', 'email', 'country', 'password')


admin.site.register(Sign_Up_Data, SignUp)
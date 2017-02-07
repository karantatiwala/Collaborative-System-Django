from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Sign_Up_Data(models.Model):
	username = models.CharField(max_length=25)
	email = models.EmailField(max_length=40)
	country = models.CharField(max_length=25)
	password = models.CharField(max_length=30)

	
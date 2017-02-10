from django.contrib import admin

# Register your models here.
from .models import Document


class Docs(admin.ModelAdmin):
	list_display = ('username','description', 'document')


admin.site.register(Document, Docs)
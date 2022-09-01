from atexit import register
from django.contrib import admin
from .models import Stock   #Stock is the class name

admin.site.register(Stock)

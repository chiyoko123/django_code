from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('quotes.urls')),  #get all the url for quotes app in the quotes urls.py file
]

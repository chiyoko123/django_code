from django.urls import path
from . import views  # dot means this directory which is quotes directory

urlpatterns = [
	path("", views.home, name="home"),  #views.function_name, "url_name" (blank means no need to type url name in the web browser)
	path("about.html", views.about, name="about"),    #name parameter is to use instead of url_name for link in html
	path('add_stock.html', views.add_stock, name="add_stock"),
	path("delete/<stock_id>", views.delete, name="delete"),
	path('delete_stock.html', views.delete_stock, name="delete_stock"),

]


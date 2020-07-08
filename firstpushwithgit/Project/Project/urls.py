"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#As from dec above
from pages.views import home_view, contacts_view, about_view

from myapp.views import (
	product_detail_view, 
	product_create_view, 
	render_initial_data, 
	dynamic_lookup_view, 
	product_delete_view, 
	products_list_view
	)

urlpatterns = [
	#include the products urls
	#path('myapp/', include('myapp.urls')),
    #set default home page to home_view from views.py
	path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('contacts', contacts_view, name='contacts'),
    path('about', about_view, name='about'),
    path('product/', product_detail_view, name='detail'),
    path('create/', product_create_view, name='create'),
    path('initial/', render_initial_data, name='initial'),
    path('lookup/<int:my_id>/', dynamic_lookup_view, name='lookup'),#lookup by id on url. U have to write lookup/number eg 2
    #You can add many more str, slugs etc
    #Url to delete
	path('lookup/<int:my_id>/delete/', product_delete_view, name='delete'),
	path('products/', products_list_view, name='products_list'),
	#For the links in products_list.html
	path('products/<int:my_id>/', dynamic_lookup_view, name='p_lookup'),
]

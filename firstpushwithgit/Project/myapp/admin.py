from django.contrib import admin

#Relative/same directory import
from .models import Product

# Register your models here.
admin.site.register(Product)

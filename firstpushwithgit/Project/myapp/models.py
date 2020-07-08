from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):#Inherits from Model
	#There are many classes of fields provided by django
	title = models.CharField(max_length=120) #maxlength required for charfield
	description = models.TextField(blank=True, null=True)
	price = models.DecimalField(decimal_places=2, max_digits=10000)#decimal_places and max_digits are reuired
	#Try add a new field and rerun the makemigarations and migrate
	summary = models.TextField(default="Very cool product")
	#makemigrations says adding a new field that is nonnullable must provide a default or set null=True
	#featured = models.BooleanField() 

	#To get the url to every product on the web page 
	def get_absolute_url(self):
		return f"{self.id}/"
		#f string or string substitution allows to grab wherever the url is such that changes in url elsewhere won't affect much
		#To make it more dynamic using url names
		#return reverse("lookup", kwargs={"id": self.id})#kwargs are the arguments that are passed
		#Reverse didn't work
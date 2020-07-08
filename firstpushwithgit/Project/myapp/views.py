from django.shortcuts import render, redirect, get_object_or_404#Raises a 404 if page is not found

from .models import Product

from .forms import ProductForm
# Create your views here.
def product_create_view(request):
	form = ProductForm(request.POST or None)
	#print(request.POST) can print in cmd what is going on
	#print(request.GET('title')) can print in cmd whatever title you gave
	if form.is_valid():
		#print(form.cleaned_data) prints in cmd the vadidated data
		#print(form.cerrors) prints in cmd the errored data
		form.save()#Saves
		#Once form is submitted rerender it to remove the inputs
		form = ProductForm()

	context = {
		'form': form
	}
	return render(request, "products/products_create.html", context)

def product_detail_view(request):
	obj = Product.objects.get(id=1)#Get object by its Id
	context = {
		#'title': obj.title,
		#'description': obj.description
		#To avoid having to change details in the views everytime the data changes we can fetch datafrom the template
		"object":obj
	}
	return render(request, "products/products_detail.html", context)

#For showing existing and initial data and updating existing data
def render_initial_data(request):
	initial_data = {
		'title': "My this awesome title"
	}
	obj = Product.objects.get(id=1)
	form = ProductForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
	context = {
		'form': form
		}
	return render(request, "products/products_create.html", context)

#For dynamic lookup of data using id
def dynamic_lookup_view(request, my_id):#my_id as referenced in urls.py
	#obj = Product.objects.get(id=my_id)
	obj = get_object_or_404(Product, id=my_id)#Raises a 404. 
	#You can also import HTTP404 and catch it in a try-except
	#try{
	#	obj = Product.objects.get(id=id)
	#except Product.DoesNotExist:
	#	raise Http404
	#} 
	context = {
		'object': obj
	}
	return render(request, "products/product_lookup.html", context)

def product_delete_view(request, my_id):
	obj = get_object_or_404(Product, id=my_id)#Raises a 404. 
	#Delete is best to use POST request
	if request.method == 'POST':
		obj.delete()
		return redirect('../../../')#A few pages back
	context = {
		'object': obj
	}
	return render(request, "products/product_delete.html", context)

def products_list_view(request):
	queryset = Product.objects.all()#Gives a list of objects

	context={
		"objects_list": queryset
	}
	return render(request, "products/products_list.html", context)
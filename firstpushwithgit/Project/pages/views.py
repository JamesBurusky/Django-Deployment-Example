from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
#You can add 'request' as the first argument and print it in cmd or print request.user to print whoever is logged in from that browser
#while if you open from incognito mode it returns 'anonymous user'
def home_view(request, *args, **kwargs):#*args and **kwargs are Python
	print(args, kwargs)
	print(request)
	print(request.user)#A variable you can use to monitor transactions
	#return HttpResponse("<h1>Hello World</h1>")
	#Return statement is always the end of a fuction. Anything after it is not run
	return render(request, "home.html", {})#Settings DIR path modified to show template location

def contacts_view(request, *args, **kwargs):
	#return HttpResponse("<h1>Contacts Page</h1>")
	my_context = {
		"title":"important people",
		"my_text":"This could be us but you code too much",
		"my_number":2243,
		"my_list":["Jesee Gituma", "Wycliffe Mutethia", "James Mwenda", "Sally Kendi"]
	}
	return render(request, "Contacts.html", my_context)#Context passed as the third argument

def about_view(request, *args, **kwargs):#*args and **kwargs are Python
	print(args, kwargs)
	print(request)
	print(request.user)#A variable you can use to monitor transactions
	#return HttpResponse("<h1>Hello World</h1>")
	#Return statement is always the end of a fuction. Anything after it is not run
	return render(request, "about.html", {})#Settings DIR path modified to show template location
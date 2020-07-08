from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
	#The fields given below can be overriden in the following way
	title = forms.CharField(label='', 
		widget=forms.TextInput(attrs={"placeholder": "Enter title"}))
	description = forms.CharField(
		required=False,
		widget=forms.Textarea(
			attrs={"placeholder":"Enter description",
				"class":"new-class-name two",
				"id": "my-id-for-textarea",
				"row":20,
				'col':120
				}
			)
		)
	price = forms.DecimalField(initial=199.99)
	#End of overriding
	class Meta:
		model = Product
		fields = [#Whatever u want to include
			'title',
			'description',
			'price'
		]

	#If some letters or words must exit in a valid input
	#def clean_title(self, *args, **kwargs):#args kwargs important when u ain't sure of the overriding
		#title = self.cleaned_data.get("title")
		#if not "CFE" in title:
		#	raise forms.ValidationError("This is not a valid title")
		#if not "new" in title:
		#	raise form.ValidationError("This is not a valid title")
		#Would work well for emails
		#if not email.endswith(".com"):
		 	#raise forms.ValidationError("This os not a valid email")
		 #return email
		#return title		
			
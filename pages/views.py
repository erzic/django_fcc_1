from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	print(f"The request is: {request}")
	print({request.user})


	return render(request=request, template_name = "home.html")

def about_view(request, *args, **kwargs):
	print(f"The request is: {request}")
	my_context = {
		"my_text": "This is about us",
		"my_number": 123,
		"my_list": [123, 456, 678, 312, "heyy"],
		"my_html": "<h1>Hello world</h1>"
	}

	return render(request=request, template_name = "about.html", 
		context = my_context)


def contact_view(request, *args, **kwargs):
	print(f"{request}")
	return render(request=request, template_name="contact.html")

def base_view(request, *args, **kwargs):
	return render(request=request, template_name="base.html")
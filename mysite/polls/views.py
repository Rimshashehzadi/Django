from django.shortcuts import render,HttpResponse      # render is use for render the template in the project 
#HttpRespone is a class in django that returns http respone 

# Create your views here.
# from django.http import HttpResponse


def index(request):
    context = {
        'variable1' : "Rimsha is great",
        'variable2' : "And Pakistan is also great country"
    }
    return render(request, 'index.html' ,context)
    # return HttpResponse("this is polls page")

def about(request):
    # return HttpResponse("this is about page")
    return render(request, 'about.html')

def services(request):
    # return HttpResponse("this is services services")
    return render(request, 'services.html')

def contact(request):
    # return HttpResponse("this is contact page")
    return render(request, 'contact.html')


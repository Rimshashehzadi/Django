from django.shortcuts import render,HttpResponse      # render is use for render the template in the project 
#HttpRespone is a class in django that returns http respone 

# Create your views here.
# from django.http import HttpResponse


def index(request):
    return HttpResponse("this is polls page")

def about(request):
    return HttpResponse("this is about page")

def services(request):
    return HttpResponse("this is services services")

def contact(request):
    return HttpResponse("this is contact page")


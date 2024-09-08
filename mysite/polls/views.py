from pyexpat.errors import messages
from django.shortcuts import render,HttpResponse  
from polls.models import Contact
from datetime import datetime     # render is use for render the template in the project 
#HttpRespone is a class in django that returns http respone 

# Create your views here.
# from django.http import HttpResponse


def index(request):
    context = {
        'variable1' : "Rimsha is great",
        'variable2' : "And Pakistan is also great country"
    }
    # messages.success(request,'this is new msg')
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
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request .POST.get('desc')
        contact = Contact(name= name,email=email,phone=phone,desc = desc, date = datetime.today())
        contact.save()
        messages.success(request,'Your message has been sent!')
        
    
    return render(request, 'contact.html')


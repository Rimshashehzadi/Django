from pyexpat.errors import messages
from django.shortcuts import redirect, render,HttpResponse  
from polls.models import Contact
from datetime import datetime 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout   # render is use for render the template in the project 
#HttpRespone is a class in django that returns http respone 

# Create your views here.
# from django.http import HttpResponse


def index(request):
    context = {
        'variable1' : "Rimsha is great",
        'variable2' : "And Pakistan is also great country"
    }
    if request.user.is_anonymous:
        return redirect('/login')
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
def loginuser(request):
    if request == 'POST':
        username = request.POST.get('username'),
        password = request.POST.get('password')
        user = authenticate(username="username", password="password")
        if user is not None:
            login(request,user)
            return redirect('/')
             # A backend authenticated the credentials
        else:
             # No backend authenticated the credentials
             return render(request,'login.html')
    return render(request, 'login.html')

def logoutuser (request):
    logout(request)
    return redirect('/login')
#user password Bisu5fB67nNY9de

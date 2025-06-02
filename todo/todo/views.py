from django . shortcuts import render,redirect
# from django.http import HttpResponse
from django.contrib.auth.models import User
from todo import models
# from todo.models import Todo
# from django.contrib.auth import authenticate

def signup(request):
    if request.method=='POST':
        frn = request.POST.get('frn')
        emailid = request.POST.get('emailid')
        pwd = request.POST.get('password')
        print(frn, emailid, pwd)
        my_user = User.objects.create_user(frn,emailid,pwd)
        my_user.save()
        return redirect('/login')
        
        # Here you would typically save the user to the database
        # For simplicity, we are just redirecting to a success page
         # Redirect to a success page or another view
    return render(request, 'signup.html')
def login(request):
    return render(request, 'login.html')
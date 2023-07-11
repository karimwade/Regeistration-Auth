from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.

def homepage(request):
    return render(request,"home.html")

def signup(request):
    if request.method=='POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        re_password = request.POST.get("re_password")
        
        if password == re_password:
            my_user = User.objects.create_user(username,email,password)
            my_user.save()
        else:
            print("Password no matching")
        print(username,email,password,re_password)
    return render(request,"signup.html")

def login(request):
    return render(request,"login.html")

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def homepage(request):
    return render(request,"home.html")

def signup(request):
    try:
        if request.method=='POST':
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")
            re_password = request.POST.get("re_password")
            
            if password == re_password:
                my_user = User.objects.create_user(username,email,password)
                my_user.save()
                return redirect("login")
            else:
                messages.info(request,"The password entered and the confirmation does not match")
            print(username,email,password,re_password)
    except IntegrityError:
        messages.warning(request,"User Already registered")
    except Exception:
        messages.warning(request,"An error has occured")
    return render(request,"signup.html")

def userLogin(request):
    if request.method=='POST':
        user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            login(request,user)
            return redirect("home")  
        else:
            messages.warning(request,"Username or Password Incorrect")

    return render(request,"login.html")

def userLogout(request):
    logout(request)
    return redirect('login')
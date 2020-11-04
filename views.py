from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    return render(request,'login.html')


def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'showloginpage.html')
        else:
            return render(request,'login.html',{'error':"invalid login credentials"})

    return render(request,'login.html')

def signup(request):
    if request.method=='POST':
        if request.POST['password']==request.POST["password-repeat"]:
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request,'base.html',{"error":"user has already been taken"})

            except User.DoesNotExist:
                user=User.objects.get(username=request.POST['username'],password=request.POST.get["password"])
                auth.authenticate(request,user)
                return redirect(home)

            else:
                return render(request,'base.html',{"error":"password doesnot match"})
    else:
        return render(request,'base.html')
def logout(request):
    auth.logout(request)
    return redirect(home)







from django.contrib.auth.models import User
from django.contrib.messages.context_processors import messages
from django.shortcuts import render, redirect


def register(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        cpassword=request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"User already exists")
                return redirect('register')
            if User.objects.filter(e=username).exists():
                messages.info(request,"User already exists")
                return redirect('register')
            if User.objects.filter(username=username).exists():
                messages.info(request,"User already exists")
                return redirect('register')
            user=User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            user.save();
            print("user created")
        else:
            print("Password not matching")
    return render(request,"register.html")
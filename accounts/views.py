from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contacts.models import *

# Create your views here.

def register(request):
    if request.POST:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password2']
        if password == password_confirm:
            if User.objects.filter(username = username).exists():
                messages.error(request,"Username Already Exits")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email Already Exits")
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                    user.save()
                    messages.success(request, "User Created Can Login")
                    return redirect('login')
        else:
            messages.error(request,"Password And Confirm Password Does not match")
            return redirect('register')

    else:
        return render(request,'accounts/register.html')

def login(request):
    if request.POST:
        if request.POST:
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username,password=password)

            if user is not None:
                auth.login(request,user)
                messages.success(request,"Logged In Successfull")
                return redirect('dashbord')
            else:
                messages.error(request,'invalid credientials')
                return redirect('login')
    else:
        return render(request,'accounts/login.html')

def logout(request):
    if request.POST:
        auth.logout(request)
        messages.success(request,'You are LoggedOut')
        return redirect('index')
    else:
        return redirect('index')

def dashbord(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context = {
        'contacts':user_contacts
    }
    return render(request,'accounts/dashbord.html',context)
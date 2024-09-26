
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create(
            username = username, 
            email = email, 
        )
        user.set_password(password)
        user.save()
        return redirect("login")
    return render(request,'auth/register.html')

def login(request):
    return render(request,'auth/login.html')



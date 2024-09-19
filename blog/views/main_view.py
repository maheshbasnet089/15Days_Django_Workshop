from django.shortcuts import render

def home(request):
    return render(request,'main/home.html')

def single_blog(request):
    return render(request,"main/single_blog.html")

def edit_blog(request):
    return render(request,"main/edit_blog.html")

def create_blog(request):
    return render(request,"main/create_blog.html")
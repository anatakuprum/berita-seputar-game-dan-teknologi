from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from post.models import *

def home(request):
    template_name = 'front/home.html'
    posting = Posting.objects.all()
    context = {
        'title' : 'Halaman Home',
        'posting' : posting,
    }
    return render(request, template_name, context)

def blog(request):
    template_name = 'front/blog.html'
    posting = Posting.objects.all()
    context = {
        'title' : 'Halaman Blog',
        'posting' : posting,
    }
    return render(request, template_name, context)

def about(request):
    template_name = 'front/about.html'
    context = {
        'title' : 'Halaman About'
    }
    return render(request, template_name, context)

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    template_name = 'account/login.html'
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            print("Account Yang Kamu Masukan Benar")
            auth_login(request, user)
            return redirect('home')
        else:
            print("Account Yang Kamu Masukan Salah")
        
    context = {
        'title' : 'Halaman Sign In'
    }
    return render(request, template_name, context)

def logout_view(request):
    logout(request)
    return redirect('home')
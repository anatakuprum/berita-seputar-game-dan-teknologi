from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import render, redirect
from post.models import *
from user.models import *

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
    posting = Posting.objects.filter(nama = request.user)
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

def detail(request, id):
    template_name = 'front/detail.html'
    posting = Posting.objects.get(id=id)
    context = {
        'title' : 'Read More',
        'posting' : posting,
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

def register(request):
    template_name = 'account/register.html'
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        alamat = request.POST.get('alamat')
        telp = request.POST.get('telp')
        try:
            with transaction.atomic():
                User.objects.create(
                    username = username,
                    password = make_password(password),
                    first_name = first_name,
                    last_name = last_name,
                    email = email,
                )
                get_user = User.objects.get(username = username)
                Biodata.objects.create(
                    user = get_user,
                    alamat = alamat,
                    telp = telp,
                )
            return redirect('home')
        except:
            pass
    context = {
        'title' : 'Halaman Register'
    }
    return render(request, template_name, context)

def logout_view(request):
    logout(request)
    return redirect('home')
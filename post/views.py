from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.db import transaction
from .forms import *
from .models import *
from user.models import *

# Create your views here.
def is_admin(user):
    if user.groups.filter(name='Admin').exists():
        return True
    else:
        return False

@login_required
def dashboard(request):
    if request.user.groups.filter(name='Admin').exists():
        request.session['is_admin'] = 'admin'
    template_name = 'back/dashboard.html'
    context = {
        'title' : 'Dashboard',
    }
    return render(request, template_name, context)

@login_required
def posts(request):
    template_name = 'back/posts.html'
    posting = Posting.objects.filter(nama = request.user)
    context = {
        'title' : 'List Posts',
        'posting' : posting,
    }
    return render(request, template_name, context)

@login_required
@user_passes_test(is_admin)
def users(request):
    template_name = 'back/users.html'
    users = User.objects.all()
    groups = Group.objects.all()
    context = {
        'title' : 'List Users',
        'users' : users,
        'groups' : groups,
    }
    return render(request, template_name, context)

@login_required
def visited(request, id):
    template_name = 'back/visited.html'
    posting = Posting.objects.get(id=id)
    context = {
        'title' : 'Lihat Postingan',
        'posting' : posting,
    }
    return render(request, template_name, context)

@login_required
def plus(request):
    template_name = 'back/plus.html'
    category = Category.objects.all()
    if request.method == "POST":
        plus = PostingForms(request.POST)  
        if plus.is_valid():
            art = plus.save(commit=False)
            art.nama = request.user
            art.save()
        return redirect(posts)
    else:
        plus = PostingForms()
    context = {
        'title' : 'Tambah Postingan',
        'category' : category,
        'plus' : plus,
    }
    return render(request, template_name, context)

@login_required
def edit(request, id):
    template_name = 'back/plus.html'
    category = Category.objects.all()
    get_posts = Posting.objects.get(id=id)
    if request.method == "POST":
        plus = PostingForms(request.POST, instance=get_posts)
        if plus.is_valid():
            art = plus.save(commit=False)
            art.nama = request.user
            art.save()
        return redirect(posts)
    else:
        plus = PostingForms(instance=get_posts)
    context = {
        'title' : 'Edit Posting',
        'category' : category,
        'get_posts' : get_posts,
        'plus': plus,
    }
    return render(request, template_name, context)

@login_required
def delete(id):
    Posting.objects.get(id=id).delete()
    return redirect(posts)

@login_required
def account(request):
    template_name = 'back/account.html'
    context = {
        'title' : 'ACCOUNT',
    }
    return render(request, template_name, context)

#Progress Edit Biodata 
def X(request, id):
    template_name = 'back/account.html'
    user = User.objects.get(username = username)
    biodata = Biodata.objects.get(id=id)
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
                user.username = username
                user.password = password
                user.first_name = first_name
                user.last_name = last_name
                user.email = email
                user.save()
                
                biodata.alamat = alamat
                biodata.telp = telp
                biodata.save()
            #     User.objects.create(
            #         username = username,
            #         password = make_password(password),
            #         first_name = first_name,
            #         last_name = last_name,
            #         email = email,
            #     )
            #     get_user = User.objects.get(username = username)
            #     Biodata.objects.create(
            #         user = get_user,
            #         alamat = alamat,
            #         telp = telp,
            #     )
            # return redirect('home')
        except:
            pass
    context = {
        'title' : 'REGISTER',
        'user' : user,
        'biodata' : biodata,
    }
    return render(request, template_name, context)
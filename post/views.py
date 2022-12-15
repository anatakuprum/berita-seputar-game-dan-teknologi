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
        'title' : 'DASHBOARD',
    }
    return render(request, template_name, context)

@login_required
def posts(request):
    template_name = 'back/posts.html'
    posting = Posting.objects.filter(nama = request.user)
    context = {
        'title' : 'LIST POSTING',
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
        'title' : 'LIST USER',
        'users' : users,
        'groups' : groups,
    }
    return render(request, template_name, context)

@login_required
def visited(request, id):
    template_name = 'back/visited.html'
    posting = Posting.objects.get(id=id)
    context = {
        'title' : 'VISITED',
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
        'title' : 'PLUS POSTING',
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
        'title' : 'EDIT POSTING',
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
def x(request):
    template_name = 'back/profile.html'
    context = {
        'title' : 'PROFILE',
    }
    return render(request, template_name, context)

#Progress Edit Biodata 
@login_required
def profile(request):
    template_name = 'back/profile.html'
    edit = User.objects.filter()
    if request.method == "POST":
        try:
            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
        
            get_user = User.objects.get(username = username)
            get_user.first_name = first_name
            get_user.last_name = last_name
            get_user.email = email
            get_user.save()
        except User.DoesNotExist:
            pass
    context = {
        'title' : 'EDIT REGISTER',
    }
    return render(request, template_name, context)
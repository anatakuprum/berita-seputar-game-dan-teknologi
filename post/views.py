from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group
from .models import *

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
    posting = Posting.objects.all()
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
        
        input_nama = request.POST.get('nama')
        input_judul = request.POST.get('judul')
        input_body = request.POST.get('body')
        input_category = request.POST.get('category')
        input_date = request.POST.get('date')
        
        #panggil kategori 
        get_category = Category.objects.get(nama=input_category)
        
        #simpan posting karena ada relasi ke tabel kategori
        Posting.objects.create(
            nama = input_nama,
            judul = input_judul,
            body = input_body,
            category = get_category,
            date = input_date,
        )
        return redirect(posts)
    context = {
        'title' : 'Tambah Postingan',
        'category' : category,
    }
    return render(request, template_name, context)

@login_required
def edit(request, id):
    template_name = 'back/plus.html'
    category = Category.objects.all()
    get_posts = Posting.objects.get(id=id)
    if request.method == "POST":
        
        input_nama = request.POST.get('nama')
        input_judul = request.POST.get('judul')
        input_body = request.POST.get('body')
        input_category = request.POST.get('category')
        input_date = request.POST.get('date')
        
        #panggil kategori 
        get_category = Category.objects.get(nama=input_category)
        
        #simpan posting karena ada relasi ke tabel kategori
        get_posts.nama = input_nama
        get_posts.judul = input_judul
        get_posts.body = input_body
        get_posts.category = get_category
        get_posts.date = input_date
        get_posts.save()
        
        return redirect(posts)
    context = {
        'title' : 'edit Posting',
        'category' : category,
        'get_posts' : get_posts,
    }
    return render(request, template_name, context)

@login_required
def delete(request, id):
    Posting.objects.get(id=id).delete()
    return redirect(posts)
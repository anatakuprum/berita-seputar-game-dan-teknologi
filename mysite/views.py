from multiprocessing import context
from re import template
from django.shortcuts import render
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
    context = {
        'title' : 'Halaman Blog'
    }
    return render(request, template_name, context)

def about(request):
    template_name = 'front/about.html'
    context = {
        'title' : 'Halaman About'
    }
    return render(request, template_name, context)
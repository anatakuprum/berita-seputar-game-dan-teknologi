from django.urls import path, include
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('posts/', posts, name='posts'),
    path('users/', users, name='users'),
    path('account/', account, name='account'),
    path('posts/plus/', plus, name='plus'),
    path('posts/visited/<int:id>', visited, name='visited'),
    path('posts/edit/<int:id>', edit, name='edit'),
    path('posts/delete/<int:id>', delete, name='delete'),
]

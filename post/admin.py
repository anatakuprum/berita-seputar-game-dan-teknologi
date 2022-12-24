from django.contrib import admin
from .models import *

# Register your models here.
class PostingAdmin(admin.ModelAdmin):
    list_display = ('nama','judul','body','category','date') 
    
class ContentAdmin(admin.ModelAdmin):
    list_display = ('title','body','image','date','link') 

admin.site.register(Category)
admin.site.register(Posting, PostingAdmin)
admin.site.register(Content, ContentAdmin)

from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Category(models.Model):
    nama = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nama
    
    class Meta:
        verbose_name_plural = "Category"

class Posting(models.Model):
    nama = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    judul = models.CharField(max_length=100)
    body = RichTextUploadingField(
        blank=True, null=True,
        config_name='special',
        external_plugin_resources=[(
            'youtube',
            '/static/ckeditor_plugins/youtube/youtube/',
            'plugin.js',
        )],
    )
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "{} - {}".format(self.nama, self.judul)
    
    class Meta:
        verbose_name_plural = "Posting"

class Content(models.Model):
    title = models.CharField(max_length=1000)
    body = models.TextField()
    image = models.ImageField()
    date = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000)
    
    def __str__(self):
        return "{} - {}".format(self.title, self.date)
    
    class Meta:
        verbose_name_plural = "Posting"
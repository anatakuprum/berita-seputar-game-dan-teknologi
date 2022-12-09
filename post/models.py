from django.contrib.auth.models import User
from django.db import models

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
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "{} - {}".format(self.nama, self.judul)
    
    class Meta:
        verbose_name_plural = "Posting"
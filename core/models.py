import datetime
import os
from re import M
from unicodedata import category
from django.db import models

def get_file_path(request, filename):
    original_file = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime, original_file)
    return os.path.join('uploads/', filename)


class Category(models.Model):
    slug = models.SlugField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True )
    img = models.ImageField(upload_to=get_file_path, null=True, blank=True )
    desc = models.TextField(max_length=500, null=True, blank=True)
    status = models.BooleanField(default=False, help_text="0=default, 1=hidden")
    trending = models.BooleanField(default=False, help_text="0=default, 1=trending")
    meta_title = models.CharField(max_length=150, null=True, blank=True)
    meta_keyword = models.CharField(max_length=150, null=True, blank=True)
    meta_desc = models.TextField(max_length=500, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name
    
    
class Product(models.Model):
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True )
    prod_img = models.ImageField(upload_to=get_file_path, null=True, blank=True )
    small_desc = models.CharField(max_length=250, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    desc = models.TextField(max_length=500, null=True, blank=True)
    no_discount_price = models.FloatField(null=True, blank=True)
    discount_price = models.FloatField(null=True, blank=True)
    status = models.BooleanField(default=False, help_text="0=default, 1=hidden")
    trending = models.BooleanField(default=False, help_text="0=default, 1=trending")
    tag = models.CharField(max_length=150, null=True, blank=True)
    meta_title = models.CharField(max_length=150, null=True, blank=True)
    meta_keyword = models.CharField(max_length=150, null=True, blank=True)
    meta_desc = models.TextField(max_length=500, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
        
    def __str__(self) -> str:
        return self.name
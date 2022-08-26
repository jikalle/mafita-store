from itertools import product
from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User

from core.models import Product

def loginPage(request):
    return render(request, 'core/login_register.html')

def logoutPage(request):
    return render(request, 'core/login_register.html')

def registerPage(request):
    return render(request, 'core/login_register.html')

def homePage(request):
    products = Product.objects.all()
    
    context = {
        'products':products
    }
    return render(request, 'core/home-page.html', context)

def profilePage(request, pk):
    profile = User.object.get(id=pk)
    
    context = {
        'profile':profile,
    }
    return render(request, 'core/profile.html', context)

def productDetail(request):
    return render(request, 'core/product-detail.html')

def cartPage(request):
    return render(request, 'core/cart.html')

def contactPage(request):
    return render(request, 'core/contact.html')

def searchPage(request):
    return render(request, 'core/search.html')
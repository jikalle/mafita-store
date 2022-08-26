from django.urls import path

from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutPage, name='logout'),
    path('register', views.registerPage, name='register-page'),
    path('profile/<int:pk>/', views.profilePage, name='profile-detail'),
    
    path('cart', views.cartPage, name='cart'),
    path('product/<int:pk>/', views.productDetail, name='product-detail'),
    
    path('contact', views.contactPage, name='contact'),
    path('search', views.searchPage, name='search'),
]
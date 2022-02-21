
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('mainpage/', views.mainpage, name="mainpage"),
    path('logout/', views.logout, name='logout'),
    path('products/',views.products,name='products'),
    path('contact/',views.contact,name='contact'),
    path('converse/',views.converse,name='converse'),
    path('adidas/',views.adidas,name='adidas'),
    path('nike/',views.nike,name='nike'),
   
    path('', views.home)
]
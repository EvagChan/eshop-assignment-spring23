from django.urls import path
from . import views
from django.contrib import admin

from django.http import HttpResponse
from django.urls import path, include



urlpatterns = [
    path('', views.home),
    path('products/', views.products),
    path('register/', views.register),
    path('contact/', views.contact),
   path('checkout/', views.checkout),
 ]

from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('home/', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('register/', views.register, name='register'),
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('home/', views.home, name='home'),
]

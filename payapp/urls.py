from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('products/', views.products, name='products'),
    path('contact/', views.contact, name='contact'),
    path('customer/', views.contact, name='customer_details'),
    path('', views.home, name='home'),
    path('customers/', views.customer_details, name='customer_details'),
]

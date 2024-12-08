# from django.shortcuts import render
#
# # Create your views here.

from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from .models import Laptop, Customer

def home(request):
    return render(request, 'home.html')
    laptops = Laptop.objects.all()
    return render(request, 'home.html', {'laptops': laptops})

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def products(request):
    return render(request, 'products.html')

def contact(request):
    return render(request, 'contact.html')


# def home(request):
#     laptops = Laptop.objects.all()
#     return render(request, 'home.html', {'laptops': laptops})

def customer_details(request):
    customers = Customer.objects.all()
    return render(request, 'customer_details.html', {'customers': customers})


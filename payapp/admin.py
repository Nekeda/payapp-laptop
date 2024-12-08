# from django.contrib import admin
#
# # Register your models here.

from django.contrib import admin
from .models import Laptop, Customer

@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'laptop', 'deposit', 'balance')

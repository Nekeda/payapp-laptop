# from django.db import models
#
# # Create your models here.

from django.db import models

class Laptop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='laptops/')

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE)
    deposit = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.balance = self.laptop.price - self.deposit
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

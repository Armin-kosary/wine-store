from django.db import models
from product.models import Product
# Create your models here.

class Order(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.PositiveIntegerField()
    price = models.PositiveIntegerField(null=True)
    products = models.ManyToManyField(Product, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

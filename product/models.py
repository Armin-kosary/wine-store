from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='product_images', null=True, blank=True)
    description = models.TextField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.title
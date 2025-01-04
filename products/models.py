from django.utils import timezone   
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=10)
    category = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    
    image = models.ImageField(
        blank=True, null=True,
        upload_to='media/products'                      
        )
    discount = models.IntegerField()

    created_date = models.DateField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
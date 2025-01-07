from django.utils import timezone   
from django.db import models

#Creación de la clase "Producto" en donde definiremos sus atributos.
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=10)
    category = models.CharField(max_length=50)
    
    #Creamos una clave foránea para referencia a Brand
    brand = models.ForeignKey(
        'products.Brand', 
        on_delete=models.CASCADE,
        related_name='products'
    )
    
    image = models.ImageField(
        blank=True, null=True,
        upload_to='media/products'                      
        )
    discount = models.IntegerField()

    created_date = models.DateField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    #Función que nos permitira que se muestren los nombres de los productos junto a la marca. 
    def __str__(self):
        return f'{self.name} | {self.brand}'
  
#Creación de la clase "Brand" en donde definiremos sus atributos.   
class Brand(models.Model):
    text = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    
    logo = models.ImageField(
        blank=True, null=True,
        upload_to='media/products'                      
        )
    
    created_date = models.DateField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
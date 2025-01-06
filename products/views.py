from django.shortcuts import render
from django.http import HttpResponse

from .models import Product

def index(request):
    #Logica 
    products = Product.objects.all()
    
    return render(request, 'List_of_products.html', 
                  {'products': products})
    
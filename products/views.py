from django.shortcuts import render

from .models import Product, Comment
from .forms import CommentsForm

def index(request):
    #Logica 
    products = Product.objects.all()
    
    return render(request, 'products/List_of_products.html', 
                  {'products': products})

def get_product(request, id):
    #Logica 
    product = Product.objects.get(id=id)
    comments = Comment.objects.filter(product=id)
    form = CommentsForm() 
    
    return render(request, 'products/show_product.html', 
                  {'product': product,
                   'comments': comments,
                   'form': form})

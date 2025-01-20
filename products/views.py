from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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

@login_required
def add_new_comment(request, id):
    if request.method == 'POST':
        
        form = CommentsForm(request.POST)
        
        if form.is_valid:
            user = request.user
            product = Product.object.get(id=id)
            
            new_comment = form.save(commit=False)
            new_comment.author = user 
            new_comment.product = product
            
            new_comment.save()
            
    return redirect('get_product', id)
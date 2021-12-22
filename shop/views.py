from django.shortcuts import render, get_object_or_404
from .models import Product, Brand, Tag, Category




def homepage(request):
    products = Product.objects.all().order_by('-created')
    return render(request, 'pages/index.html', {'products': products})

def shop(request):
    products = Product.objects.all().order_by('-created')
    return render(request, 'pages/shop.html', {'products': products})

def product_details(request, pk):
    # product = Product.objects.filter(pk = pk)
    product = get_object_or_404(Product,pk = pk)
    print(product)
    return render(request, 'pages/product-details.html', {'product': product})

def shop_cart(request):
    return render(request, 'pages/shop-cart.html')

def checkout(request):
    return render(request, 'pages/checkout.html')

def contact(request):
    return render(request, 'pages/contact.html')
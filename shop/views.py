from django.shortcuts import render
from .models import Product, Brand, Tag, Category




def homepage(request):
    products = Product.objects.all().order_by('-created')
    return render(request, 'pages/index.html', {'products': products})

def shop(request):
    return render(request, 'pages/shop.html')

def product_details(request):
    return render(request, 'pages/product-details.html')

def shop_cart(request):
    return render(request, 'pages/shop-cart.html')

def checkout(request):
    return render(request, 'pages/checkout.html')

def contact(request):
    return render(request, 'pages/contact.html')
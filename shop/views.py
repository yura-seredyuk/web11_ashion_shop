from django.shortcuts import render


def homepage(request):
    return render(request, 'pages/index.html')

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
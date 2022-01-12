from django.shortcuts import render, get_object_or_404
from .models import Product, Brand, Tag, Category, Colors


def homepage(request):
    products = Product.objects.all().order_by('-created')
    return render(request, 'pages/index.html', {'products': products})

def shop(request, tag_slug=None, category_slug=None):
    tags = Tag.objects.all()
    categories = Category.objects.all()
    brands = Brand.objects.all()
    colors = Colors.objects.all()
    

    if category_slug:
        tag = Tag.objects.filter(slug=tag_slug)[0]
        category = Category.objects.filter(slug=category_slug)[0]
        products = Product.objects.filter(tag=tag, category=category).order_by('-created')    
    
    elif tag_slug:
        tag = Tag.objects.filter(slug=tag_slug)[0]
        products = Product.objects.filter(tag=tag).order_by('-created')    
    
    else:
        products = Product.objects.all().order_by('-created')

    if products:
        min_price = max_price = products[0].price
        for product in products:
            if product.price < min_price:
                min_price = product.price
            if product.price > max_price:
                max_price = product.price 
    else:
        min_price = max_price = 0
        
    if request.method == 'POST':
        print(request)

    return render(request, 'pages/shop.html', {'products': products,
                                                'tags':tags,
                                                'categories':categories,
                                                'brands':brands,
                                                'colors':colors,
                                                'min_price': int(min_price),
                                                'max_price': int(max_price)})

def product_details(request, pk):
    product = get_object_or_404(Product,pk = pk)
    colors = product.colors.all()
    print(colors)
    return render(request, 'pages/product-details.html', {'product': product,
                                                          'colors': colors})

def shop_cart(request):
    return render(request, 'pages/shop-cart.html')

def checkout(request):
    return render(request, 'pages/checkout.html')

def contact(request):
    return render(request, 'pages/contact.html')
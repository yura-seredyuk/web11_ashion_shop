from django.shortcuts import render, get_object_or_404
from .models import Product, Brand, Tag, Category, Colors


def homepage(request):
    products = Product.objects.all().order_by('-created')
    return render(request, 'pages/index.html', {'products': products})

def shop(request, tag_slug=None, category_slug=None):
    tags = Tag.objects.all()
    categories = Category.objects.all()
    brands = Brand.objects.all()
    
    available_colors = []
    selected_colors = []

    if request.method == 'POST':
        selected_colors = request.POST.getlist('colors')
        if selected_colors:
            colors = Colors.objects.filter(color__in=selected_colors)
        else:
            colors = Colors.objects.all()
        print(selected_colors)
        print(colors)
    else:
        colors = Colors.objects.all()
 

    # if selected_colors:
    #     products = Product.objects.filter(colors__in=colors)

    if category_slug:
        tag = Tag.objects.filter(slug=tag_slug)[0]
        category = Category.objects.filter(slug=category_slug)[0]
        products = Product.objects.filter(tag=tag, category=category, colors__in=colors).order_by('-created').distinct()    
    
    elif tag_slug:
        tag = Tag.objects.filter(slug=tag_slug)[0]
        products = Product.objects.filter(tag=tag, colors__in=colors).order_by('-created').distinct()    
    
    else:
        products = Product.objects.filter(colors__in=colors).order_by('-created').distinct()

    
    if products:
        min_price = max_price = products[0].price
        for product in products:
            if product.price < min_price:
                min_price = product.price
            if product.price > max_price:
                max_price = product.price
            # ------- get colors
            for color in product.colors.all():
                if color not in available_colors:
                    available_colors.append(color)                   
    else:
        min_price = max_price = 0



    return render(request, 'pages/shop.html', {'products': products,
                                                'tags':tags,
                                                'categories':categories,
                                                'brands':brands,
                                                # 'colors':colors,
                                                'min_price': int(min_price),
                                                'max_price': int(max_price),
                                                'available_colors':available_colors,
                                                'selected_colors': selected_colors})

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
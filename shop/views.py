import json
from django.shortcuts import render, get_object_or_404
from myauth.models import Profile
from django.contrib.auth.models import User
from cart.cart import Cart
from cart.forms import CartAddProductForm
from .models import Product, Brand, Tag, Category, Colors,\
                    Sizes, Order
from django.conf import settings

from django.core.paginator import Paginator
from decimal import Decimal

from django.core.mail import EmailMessage


def homepage(request):
    products = Product.objects.all().order_by('-created')
    return render(request, 'pages/index.html', {'products': products,
                                                'cart': shop_cart(request)})

def shop(request, tag_slug=None, category_slug=None, search=None):
    tags = Tag.objects.all()
    categories = Category.objects.all()
    brands = Brand.objects.all()
    
    available_colors = []
    selected_colors = []

    available_sizes = []
    selected_sizes = []   

    if request.method == 'POST':
        selected_colors = request.POST.getlist('colors')
        if selected_colors:
            colors = Colors.objects.filter(color__in=selected_colors)
        else:
            colors = Colors.objects.all()
        print(selected_colors)
        print(colors)
        sizes = Sizes.objects.all()
    else:
        colors = Colors.objects.all()
        sizes = Sizes.objects.all()
    
    if request.method == 'POST':
        if request.POST.get('search_input'):
            search = request.POST.get('search_input').lower() 

    if category_slug:
        tag = Tag.objects.filter(slug=tag_slug)[0]
        category = Category.objects.filter(slug=category_slug)[0]
        products = Product.objects.filter(tag=tag, category=category, colors__in=colors).order_by('-created').distinct()    
    
    elif tag_slug:
        tag = Tag.objects.filter(slug=tag_slug)[0]
        products = Product.objects.filter(tag=tag, colors__in=colors).order_by('-created').distinct()    
    elif search:
        products = Product.objects.filter(slug__contains=search).order_by('-created').distinct()
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

    cart_product_form = CartAddProductForm()

    paginator = Paginator(products, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'pages/shop.html', {'products': products,
                                                'tags':tags,
                                                'categories':categories,
                                                'brands':brands,
                                                # 'colors':colors,
                                                'sizes':sizes,
                                                'min_price': int(min_price),
                                                'max_price': int(max_price),
                                                'available_colors':available_colors,
                                                'selected_colors': selected_colors,
                                                'selected_sizes': selected_sizes,
                                                'cart_product_form':cart_product_form,
                                                'cart': shop_cart(request),
                                                'page_obj': page_obj})

def product_details(request, pk):
    product = get_object_or_404(Product,pk = pk)
    colors = product.colors.all()
    print(colors)
    cart_product_form = CartAddProductForm()
    return render(request, 'pages/product-details.html', {'product': product,
                                                          'colors': colors,
                                                          'cart_product_form':cart_product_form,
                                                          'cart': shop_cart(request)})

def shop_cart(request):
    cart = request.session.get(settings.CART_SESSION_ID)
    count = subtotal = total =  0
    product_list = 0
    products = []

    if cart:
        cart_values = cart.values()
        for item in cart_values:
            count += item['quantity']
            subtotal += item['quantity'] * float(item['price'])

        cart_items_id = cart.keys()
        product_list = Product.objects.filter(id__in=cart_items_id)
        cart = Cart(request)

        for product in  product_list:
            cart_item = {}
            cart_item['product'] = product
            cart_item['quantity'] = cart.cart[f'{product.id}']['quantity']
            products.append(cart_item)
            
            

    return {'count': count, 
            'product_list':product_list, 
            'subtotal':subtotal, 
            'cart':cart, 
            'products': products}

def checkout(request):        
    return render(request, 'pages/checkout.html', {'cart': shop_cart(request)})

def order(request):
    cart = Cart(request)
    order = Order()
    order.order_data =json.dumps(cart.cart)
    order.subtotal = sum(int(item['quantity']) * float(item['price']) for item in 
                    cart.cart.values())
    # user = User.objects.filter(username='user')
    # order.profile_id = Profile.objects.filter(id=user)   
    order.save()             
    return render(request, 'pages/order.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        site = request.POST['site']
        message = request.POST['message']
        subject = f'Subject: {name} - {site}'
        body = f'{message} \nContact email: {email}'
        email = EmailMessage(subject, body, to=['yurii.seredyuk@gmail.com'])
        email.send()
    return render(request, 'pages/contact.html', {'cart': shop_cart(request)})
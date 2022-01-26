from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from shop.views import shop_cart as cart


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    form = CartAddProductForm(request.POST)
    print(form)
    print(form.is_valid(), form.errors)
    if form.is_valid():
        print(form.cleaned_data)
        c_d = form.cleaned_data
        cart.add(product=product, 
                quantity=c_d['quantity'],
                update_quantity=c_d['update'])
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart_data = Cart(request)
    if request.method == 'POST':
        print(request.POST.get('qty_5',''))
    return render(request, 'cart/detail.html', 
                    {'cart':cart(request), 
                    'cart_data':cart_data, 
                    'count':cart_data.__len__()}) 

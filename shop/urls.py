from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('shop/', views.shop, name='shop'),
    path('shop/<tag_slug>/', views.shop, name='shop'),
    path('shop/<tag_slug>/<category_slug>', views.shop, name='shop'),
    path('product-details/<int:pk>', views.product_details, name='product-details'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
]
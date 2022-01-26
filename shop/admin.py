from django.contrib import admin
from django.db import models
from .models import Category, Tag, Brand, Product, Colors,\
                    Sizes, Order


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)

class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'country']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Brand, BrandAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Tag, TagAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'old_price', 'rait', 'available', 'quantity', 'created']
    list_filter = ['rait', 'available', 'created', 'tag', 'brand', 'category']
    list_editable = ['price', 'old_price', 'available', 'quantity']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Product, ProductAdmin)

class ColorsAdmin(admin.ModelAdmin):
    list_display = ['color']
    

admin.site.register(Colors, ColorsAdmin)


class SizesAdmin(admin.ModelAdmin):
    list_display = ['size']
    

admin.site.register(Sizes, SizesAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile_id', 'created', 'subtotal', 'status']
    list_filter = ['created','status']
    list_editable = ['status']

admin.site.register(Order, OrderAdmin)
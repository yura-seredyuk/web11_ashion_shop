from django.contrib import admin
from django.db import models
from .models import Category, Tag, Brand, Product


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
    list_display = ['name', 'slug', 'price', 'old_price', 'rait', 'available', 'quantity']
    list_filter = ['rait', 'available', 'created', 'tag', 'brand', 'category']
    list_editable = ['price', 'old_price', 'available', 'quantity']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Product, ProductAdmin)


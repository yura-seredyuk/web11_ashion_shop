from django.db import models
from django.db.models.deletion import SET_NULL


class Brand(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    country = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reversed('shop:product_list_by_brand', args=[self.slug])

class Product(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    brand = models.ForeignKey(Brand, related_name='products', null=True, on_delete=SET_NULL)
    main_photo = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    photo_1 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    photo_2 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    photo_3 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
   
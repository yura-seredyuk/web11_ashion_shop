from django.db import models
from django.db.models.deletion import SET_NULL
from django.db.models.query_utils import PathInfo
from django.urls import reverse
from datetime import date, timedelta, datetime
import pytz

utc=pytz.UTC

class Brand(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    country = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_brand', args=[self.slug])

class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ("name",)
        verbose_name = 'Category',
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Tag(models.Model):
    """
    select: Men's, Women's, Kid's
    """
    TAGS = (
        ('men', "Men's"),
        ('women', "Women's"),
        ('kid', "Kid's"),
    )
    name = models.CharField(max_length=10, choices=TAGS, default='men')
    slug = models.SlugField(max_length=10, unique=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_tag', args=[self.slug])

class Colors(models.Model):
    color = models.CharField(max_length=30)
    
    class Meta:
        ordering = ['color']
        verbose_name = 'Colors',
        verbose_name_plural = 'Colors'

    def __str__(self):
        return self.color

class Product(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    brand = models.ForeignKey(Brand, related_name='products', null=True, on_delete=SET_NULL)
    tag = models.ForeignKey(Tag, related_name='products', null=True, on_delete=SET_NULL)
    category = models.ForeignKey(Category, related_name='products', null=True, on_delete=SET_NULL)
    main_photo = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    photo_1 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    photo_2 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    photo_3 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    details = models.TextField() # short details
    description = models.TextField()
    specification = models.TextField()
    # reviews
    price = models.DecimalField(max_digits=10, decimal_places=1, blank=True)
    old_price = models.DecimalField(max_digits=10, decimal_places=1, null=True, blank=True)
    available = models.BooleanField(default=True)
    quantity = models.IntegerField(default=5)
    rait = models.PositiveIntegerField(default=0)
    review_count = models.IntegerField(default=0)
    colors = models.ManyToManyField(Colors)
    # sizes
    promotions = models.CharField(max_length=50, default='Free shipping')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("name",)
        index_together = (('id', 'slug'),)

    def __str__(self) -> str:
        return self.name


    @property
    def is_new(self):
        """
        params: days_count for mark new products
        """
        days_count = 1
        new_date = utc.localize(datetime.today() - timedelta(days=days_count))
        diff = (new_date-self.created).days
        if diff < 0 and self.available:
            return True
        else:
            return False

    @property
    def is_sale(self):
        """
        params: days_count for sale products
        """
        days_count = 1
        new_date = utc.localize(datetime.today() - timedelta(days=days_count))
        diff = (new_date-self.created).days
        if diff >= 0 and self.available:
            return True
        else:
            return False

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

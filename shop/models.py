from django.db import models
from django.db.models.deletion import SET_NULL
from django.urls import reverse


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
    select: Men's, Women's
    """
    TAGS = (
        ('men', "Men's"),
        ('womens', "Women's"),
    )
    name = models.CharField(max_length=10, choices=TAGS, default='men')
    slug = models.SlugField(max_length=10, unique=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_tag', args=[self.slug])

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
    price = models.DecimalField(max_digits=10, decimal_places=1)
    old_price = models.DecimalField(max_digits=10, decimal_places=1, blank=True)
    available = models.BooleanField(default=True)
    quantity = models.IntegerField(default=5)
    rait = models.PositiveIntegerField(default=0)
    review_count = models.IntegerField(default=0)
    # colors
    # sizes
    promotions = models.CharField(max_length=50, default='Free shipping')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("name",)
        index_together = (('id', 'slug'),)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

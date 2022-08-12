from distutils.command.upload import upload
from secrets import choice
from unicodedata import category
from django.db import models
from django.utils import timezone

# Create your models here.


class Product_category(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.CharField(max_length=3000, null=True, blank=True)
    thumbnail = models.ImageField()

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=250, unique=True)
    category = models.ForeignKey(
        Product_category, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=3000)
    thumbnail = models.ImageField(upload_to="products/thumbnail")
    cost_price = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True)
    marked_price = models.DecimalField(max_digits=8, decimal_places=2)
    discount_price = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True)
    count_in_stock = models.IntegerField(null=True, blank=True)
    status_choices = (('AVAILABLE', 'Available'),
                      ('OUT OF STOCK', 'Out of Stock'))
    status = models.TextField(choices=status_choices,
                              max_length=250, default=status_choices[0][1])
    rating = models.DecimalField(
        max_digits=3, decimal_places=2, null=True, blank=True)
    review = models.IntegerField(null=True, blank=True)
    state = models.BooleanField(
        help_text="On makes item visible, off hides it", default=True)
    publish = models.DateTimeField(default=timezone.now, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null= True)

    def __str__(self):
        return self.title


class Product_image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.FileField(null=True, blank=True)
    alt_text = models.CharField(max_length=150, null=True, blank=True)


class Carousel(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='carousel/')
    description = models.TextField(null=True, blank=True)
    state = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title


# order models


class Order(models.Model):
    paid = models.BooleanField(default=False)
    c_name = models.CharField(max_length=250)
    c_email = models.EmailField(null=True, blank=True)
    c_phone = models.IntegerField()
    c_address = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="products", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
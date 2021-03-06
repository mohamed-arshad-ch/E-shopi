from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class User(AbstractUser):
# 	passww = models.CharField(max_length=200, null=True, blank=True)


class Customer(models.Model):
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    device = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        if self.name:
            name = self.name
        else:
            name = self.device
        return str(name)


class Category(models.Model):
    cname = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.cname


class Product(models.Model):
    name = models.CharField(max_length=200)
    cname = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    qty = models.IntegerField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Wishlist(models.Model):
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    product_id = models.IntegerField()
    name = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, blank=True)
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(null=True, blank=True)


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)
    device = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return "%s %s" % (self.customer, self.device)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    # @property
    # def get_cart_items(self):
    # 	orderitems = self.orderitem_set.all()
    # 	total = sum([item.quantity for item in orderitems])
    # 	return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    complete = models.BooleanField(default=False)
    status_track = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address1 = models.CharField(max_length=200, null=False)
    address2 = models.CharField(max_length=200, null=False)
    address3 = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.customer)


class Userotp(models.Model):
    name = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12)
    passw = models.CharField(max_length=120)

    def __str__(self):
        return self.phone

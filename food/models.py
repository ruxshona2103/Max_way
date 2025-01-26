from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=300, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'category'


    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=300, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    cost = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    image = models.ImageField(upload_to="products")

    class Meta:
        db_table = 'product'


    def __str__(self):
        return self.title


class Customer(models.Model):
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    phone_number = models.IntegerField(max_length=13)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'customer'

    def __str__(self):
        return self.first_name

class Order(models.Model):
    payment_type = models.IntegerField(null=False, blank=False)
    status = models.IntegerField(null=False, blank=True, default=1)
    address = models.CharField(null=False, blank=False, max_length=300)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, max_length=250, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'order'






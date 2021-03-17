from django.db import models
import datetime


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, blank=False)
    price = models.IntegerField(default=0, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, blank=False)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_product_by_id(ids):
        return Product.objects.filter(id__in=ids)


class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + " " + self.last_name

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def emailExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        else:
            return False


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='')
    phone = models.CharField(max_length=50, default='')
    date = models.DateTimeField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order \
            .objects \
            .filter(customer=customer_id)\
            .order_by('-date')


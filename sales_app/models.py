from django.db import models

# Create your models here.
class Products(models.Model):
    prod_name = models.TextField()
    prod_description = models.TextField()
    prod_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.TextField()

    def __str__(self):
        return self.prod_name + ' ' + self.prod_description
    
class Orders(models.Model):
    order_date = models.DateField()
    order_total = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.TextField()
    customer_name = models.TextField()
    customer_address = models.TextField()
    customer_phone = models.TextField()
    customer_email = models.TextField()
    order_items = models.ManyToManyField(Products)

    def __str__(self):
        return self.customer_name + ' ' + self.order_status
from django.db import models

# Create your models here.
class Products(models.Model):

    prod_name = models.TextField()
    prod_description = models.TextField()
    pp_no = models.TextField()
    prod_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.TextField()

    def __str__(self):
        return self.prod_name + '\n' + self.prod_description
    
class Orders(models.Model):
    order_date = models.DateField()
    order_total = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.TextField()
    customer_name = models.TextField()
    customer_address = models.TextField()
    customer_phone = models.TextField()
    customer_email = models.TextField()
    order_item = models.ForeignKey(Products,on_delete=models.CASCADE,related_name="orders_item",)

    def __str__(self):
        return self.customer_name + '\n' + self.order_status
    
class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_body = models.TextField()  

    def __str__(self):
        return self.blog_title
    
class Comment(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name="comments")
    comment = models.TextField()

    def __str__(self):
        return self.comment
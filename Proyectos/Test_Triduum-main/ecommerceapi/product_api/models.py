from django.db import models
from django.db import connection

# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    stock = models.IntegerField()

    def __str__(self):
        return self.name

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    client = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)

class OrderDetail(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order, related_name= 'order_details', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    product_id = models.ForeignKey(Product, related_name= 'order_products', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('order_id', 'product_id')
        ordering = ['id']

    def __str__(self):
        return str(self.order_id, self.product_id)
    

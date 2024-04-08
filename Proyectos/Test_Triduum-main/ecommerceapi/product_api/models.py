from django.db import models

class Product(models.Model):
    """
    Represents a product in the inventory.

    Attributes:
        id (AutoField): The unique identifier for the product.
        name (CharField): The name of the product.
        price (FloatField): The price of the product.
        stock (IntegerField): The available stock of the product.
    """

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    stock = models.IntegerField()

    def __str__(self):
        """
        Returns a string representation of the product.
        """
        return self.name

class Order(models.Model):
    """
    Represents an order placed by a client.

    Attributes:
        id (AutoField): The unique identifier for the order.
        date (DateField): The date when the order was placed.
        client (CharField): The name of the client who placed the order.
    """

    id = models.AutoField(primary_key=True)
    date = models.DateField()
    client = models.CharField(max_length=200)

    def __str__(self):
        """
        Returns a string representation of the order.
        """
        return str(self.id)

class OrderDetail(models.Model):
    """
    Represents the details of an order, including the products ordered.

    Attributes:
        id (AutoField): The unique identifier for the order detail.
        order_id (ForeignKey): The order to which this detail belongs.
        quantity (IntegerField): The quantity of the product ordered.
        product_id (ForeignKey): The product ordered.
    """

    id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(
        Order, related_name='order_details', on_delete=models.CASCADE
    )
    quantity = models.IntegerField()
    product_id = models.ForeignKey(
        Product, related_name='order_products', on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('order_id', 'product_id')
        ordering = ['id']

    def __str__(self):
        """
        Returns a string representation of the order detail.
        """
        return f"Order ID: {self.order_id}, Product ID: {self.product_id}"

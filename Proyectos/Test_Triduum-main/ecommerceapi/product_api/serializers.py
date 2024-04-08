from rest_framework import serializers
from product_api.models import Product, Order, OrderDetail

class ProductSerializer(serializers.ModelSerializer):
    """
    Serializes Product objects.

    Attributes:
        model (Product): The Product model to serialize.
        fields (list): The fields to include in the serialization.
    """

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'stock']

class OrderDetailSerializer(serializers.ModelSerializer):
    """
    Serializes OrderDetail objects.

    Attributes:
        model (OrderDetail): The OrderDetail model to serialize.
        fields (list): The fields to include in the serialization.
    """

    class Meta:
        model = OrderDetail
        fields = ['id', 'order_id', 'quantity', 'product_id']

class OrderSerializer(serializers.ModelSerializer):
    """
    Serializes Order objects.

    Attributes:
        order_details (OrderDetailSerializer): Serializer for OrderDetail objects.
        model (Order): The Order model to serialize.
        fields (list): The fields to include in the serialization.
    """

    order_details = OrderDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'date', 'client', 'order_details']

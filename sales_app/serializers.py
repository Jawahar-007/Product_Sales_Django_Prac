from rest_framework import serializers
from .models import Products, Orders

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"

class OrdersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = "__all__"
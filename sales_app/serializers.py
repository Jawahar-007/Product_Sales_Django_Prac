from rest_framework import serializers
from .models import Products, Orders , Blog , Comment

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"

class OrdersSerializers(serializers.ModelSerializer):
    orders_item = ProductSerializers(many=True,read_only = True) # Note: Name given in related_name in model foreignKey 
    class Meta:                                            # should be used as object name 'order'.
        model = Orders
        fields = "__all__"

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class BlogSerializers(serializers.ModelSerializer):
    comments = CommentSerializers(many=True,read_only = True)
    class Meta:
        model = Blog
        fields = "__all__" # Note: Only fields mentioned in fields will be displayed in response.

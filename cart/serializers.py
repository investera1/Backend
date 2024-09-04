from rest_framework import serializers
from .models import Cart
from product.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'product_image', 'description', 'store']

class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)  # Use a nested serializer

    class Meta:
        model = Cart
        fields = '__all__'  # Adjust fields as needed

    def create(self, validated_data):
        # Extract product ID or reference
        product_data = validated_data.pop('product')
        product = Product.objects.get(id=product_data['id'])

        # Create the cart entry
        cart = Cart.objects.create(product=product, **validated_data)
        
        return cart

from rest_framework import serializers
from .models import Type, Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    type = TypeSerializer(read_only=True)
    class Meta:
        model = Product
        fields = ('id', 'name', 'barcode', 'category', 'type', 'price', 'off_price', 'off_percent', 'image')
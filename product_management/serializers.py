from .models import Product, Category
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']

        # def create(cls, valideated_data):
        #     category = Category.objects.create(
        #         category_name = valideated_data['category_name']
        #     )
        #     category.save()
        #     return category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name', 'product_category']

        # def create(cls, validated_data):
        #     product = Product.objects.create(
        #         product_name = validated_data['product_name'],
        #         product_category = validated_data['product_category']
        #     )
        #     product.save()
        #     return product
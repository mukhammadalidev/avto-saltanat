from rest_framework import serializers
from .models import Product

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    
    def create(self,validated_data):
        product = Product.objects.create(**validated_data)

        return product
from rest_framework import serializers
from .models import Product,CategoryModel,technical_specification



    


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = "__all__"

    
    def create(self,validated_data):
        category = CategoryModel.objects.create(**validated_data)

        return category
    
class technical_specificationSerializers(serializers.ModelSerializer):
    class Meta:
        model = technical_specification
        fields = "__all__"

    
    def create(self,validated_data):
        category = CategoryModel.objects.create(**validated_data)

        return category
    

class ProductSerializers(serializers.ModelSerializer):
    category = CategorySerializers()
    technical_specification = technical_specificationSerializers()
    class Meta:
        model = Product
        fields = "__all__"

        
    def create(self,validated_data):
        product = Product.objects.create(**validated_data)

        return product
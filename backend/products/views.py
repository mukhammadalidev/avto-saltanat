from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProductSerializers,CategorySerializers
from .models import Product,CategoryModel

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializers
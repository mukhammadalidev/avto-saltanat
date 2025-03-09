from django.shortcuts import render
from rest_framework import viewsets
from .serializers import NewsSerializers
from .models import New

class NewsViewSet(viewsets.ModelViewSet):
    queryset = New.objects.all()
    serializer_class = NewsSerializers
from rest_framework import serializers
from .models import New

class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = "__all__"

    
    def create(self,validate_data):

        news = New.objects.create(**validate_data)

        return news
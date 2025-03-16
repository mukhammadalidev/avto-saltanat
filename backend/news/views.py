from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .models import New
from rest_framework.viewsets import ModelViewSet
from .serializers import NewsSerializers

class NewsViewSet(ModelViewSet):
    queryset = New.objects.all()
    serializer_class = NewsSerializers

    def perform_create(self, serializer):
        news = serializer.save()
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "news_updates",
            {
                "type": "send_news_update",
                "news": NewsSerializers(news).data,
            },
        )

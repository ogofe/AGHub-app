from core.models import (
    Announcement,
    Event,
    Sermon
)
from rest_framework.serializers import ModelSerializer

class AnnouncementSerializer(ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'
        lookup_field = 'id'

class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        lookup_field = 'id'

class SermonSerializer(ModelSerializer):
    class Meta:
        model = Sermon
        fields = '__all__'
        lookup_field = 'title'
from django.shortcuts import render
from rest_framework.viewsets import generics
from core.models import (
    Announcement,
    Event,
    Sermon
)
from .serializers import (
    AnnouncementSerializer,
    EventSerializer,
    SermonSerializer
)

class Announcements(generics.ListAPIView):
    queryset = Announcement.objects.all()
    model = Announcement
    serializer_class = AnnouncementSerializer

class Events(generics.ListAPIView):
    queryset = Event.objects.all()
    model = Event
    serializer_class = EventSerializer

class Sermons(generics.ListAPIView):
    queryset = Sermon.objects.all()
    model = Sermon
    allowed_methods = ['GET',]
    serializer_class = SermonSerializer
    

class SermonSearch(generics.RetrieveAPIView):
    queryset = Sermon.objects.all()
    model = Sermon
    lookup_field = 'title'
    serializer_class = SermonSerializer

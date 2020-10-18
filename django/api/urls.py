from .views import (
    Announcements,
    Events,
    Sermons,
    SermonSearch
)
from django.urls import path

app_name = 'api'

urlpatterns = [
    path('news/', Announcements.as_view(), name='news'),
    path('events/', Events.as_view(), name='events'),
    path('sermons/', Sermons.as_view(), name='sermons'),
    path('sermons/<title>', SermonSearch.as_view(), name='sermon'),
]


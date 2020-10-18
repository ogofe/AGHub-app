from django.contrib import admin
from .models import (
        Announcement,
        Event,
        EventType,
        Sermon
    )


class AdminAnnouncement(admin.ModelAdmin):
    model = Announcement
    search_fields = [
        'date',
        'content'
    ]
    list_disply= [
        'date',
        'announcements',
    ]

class AdminEvent(admin.ModelAdmin):
    model = Event
    list_disply= [
        'name',
        'date',
        'status',
    ]

class AdminEventType(admin.ModelAdmin):
    model = EventType
    list_disply= [
        'title',
    ]

class AdminSermon(admin.ModelAdmin):
    model = Sermon
    list_disply= [
        'speaker',
        'title',
        'date',
    ]
    search_fields = [
        'speaker',
        'title',
        'date'
    ]
    
# Register your models here.
admin.site.register(Sermon, AdminSermon)
admin.site.register(Announcement, AdminAnnouncement)
admin.site.register(Event, AdminEvent)
admin.site.register(EventType, AdminEventType)
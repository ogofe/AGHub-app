from django.db import models

# Create your models here.
class Sermon(models.Model):
    title = models.CharField(max_length=350)
    sub_title = models.CharField(max_length=350, blank=True)
    file = models.FileField(upload_to='media/')
    description = models.TextField(blank=True)
    speaker = models.CharField(max_length=200, default="Rev. Sunday James Ekele")
    date  = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.title

STATUS = (
    ('open', "Open"),
    ('closed', "Closed"),
    ('postponed', "Postponed")
)

class EventType(models.Model):
    title = models.CharField(max_length=150)
    
    def __str__(self):
        return self.title

class Event(models.Model):
    name  = models.CharField(max_length=500, unique=True)
    image = models.ImageField(blank=True, upload_to='events/')
    date  = models.DateField()
    time  = models.TimeField()
    venue = models.TextField()
    _type = models.ForeignKey("EventType", on_delete=models.DO_NOTHING)
    status= models.CharField(max_length=30, choices=STATUS)
    
    
    def __str__(self):
        return self.name
    
class Announcement(models.Model):
    date = models.DateField(auto_now=True)
    content = models.TextField()
    
    def __str__(self):
        return str(self.date)
    
    def announcements(self):
        return self.objects.all().count()
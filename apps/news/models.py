from django.db import models

# Create your models here.

EVENTS = [
    ('upcoming', 'upcoming'),
    ('past', 'past'),
    ('retired', 'retired')
]

TYPES = [
    ('upcoming event', 'upcoming'),
    ('app update', 'app'),
    ('online competition', 'online'),
    ('past event', 'past')
]

PRIORITY = [
    ('large', 'large'),
    ('small', 'small')
]


class Event(models.Model):
    """Model representing details of upcoming event"""
    types = models.CharField(max_length=100, choices=TYPES)
    priority = models.CharField(max_length=50, choices=PRIORITY)
    title = models.CharField(max_length=40)
    timing = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=500, blank=True)
    description1 = models.CharField(max_length=1000, blank=True)
    url = models.URLField(max_length=200)
    image = models.ImageField(upload_to='news', blank=True)
    status = models.CharField(max_length=10, choices=EVENTS)

    class Meta:
        app_label = 'news'
        db_table = 'events'

    def __str__(self):
        return self.title


class EventUpdate(models.Model):
    """Model representing event update"""
    title = models.CharField(max_length=40)
    timing = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=500, blank=True)
    description1 = models.CharField(max_length=500)
    description2 = models.CharField(max_length=500)
    description3 = models.CharField(max_length=500)
    url = models.URLField(max_length=200)
    image = models.ImageField(upload_to='news')
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    class Meta:
        app_label = 'news'
        db_table = 'event updates'

    def __str__(self):
        return self.title

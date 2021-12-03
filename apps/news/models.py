from django.db import models

# Create your models here.

TYPES = [
    ('ongoing event', 'ongoing'),
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
    shortDescription = models.CharField(max_length=500, blank=True)
    fullDescription = models.CharField(max_length=1000, blank=True)
    url = models.URLField(max_length=200)
    image = models.ImageField(upload_to='news', blank=True)
    is_visible = models.BooleanField(default=True)

    class Meta:
        app_label = 'news'
        db_table = 'events'

    def __str__(self):
        return self.title


class EventUpdate(models.Model):
    """Model representing event update"""
    title = models.CharField(max_length=40)
    timing = models.CharField(max_length=50, blank=True, default='')
    description = models.CharField(max_length=500, blank=True)
    contactInfo = models.CharField(max_length=500, blank=True)
    footNote = models.CharField(max_length=500, blank=True)
    greetings = models.CharField(max_length=500, blank=True)
    url = models.URLField(max_length=200, blank=True)
    image = models.ImageField(upload_to='news', blank=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    class Meta:
        app_label = 'news'
        db_table = 'event updates'

    def __str__(self):
        return self.title

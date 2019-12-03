from django.db import models

# Create your models here.

EVENTS = [
    ('upcoming', 'upcoming'),
    ('past1', 'past1'),
    ('past2', 'past2')
]


class Event(models.Model):
    """Model representing details of upcoming event"""
    title = models.CharField(max_length=40)
    timing = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    description1 = models.CharField(max_length=1000)
    url = models.URLField(max_length=200)
    image = models.ImageField(upload_to='news')
    status = models.CharField(max_length=10, choices=EVENTS)

    class Meta:
        app_label = 'news'
        db_table = 'upcoming event'

    def __str__(self):
        return self.title


class AppUpdate(models.Model):
    """Model representing app updates"""
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=500)
    url = models.URLField(max_length=200)

    class Meta:
        app_label = 'news'
        db_table = 'app update'

    def __str__(self):
        return self.title


class OnlineCompetition(models.Model):
    """Model representing details of online competition"""
    title = models.CharField(max_length=40)
    timing = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    url = models.URLField(max_length=200)

    class Meta:
        app_label = 'news'
        db_table = 'online competition'

    def __str__(self):
        return self.title


class EventUpdate(models.Model):
    """Model representing event update"""
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=500)
    description1 = models.CharField(max_length=500)
    description2 = models.CharField(max_length=500)
    url = models.URLField(max_length=200)
    image = models.ImageField(upload_to='news')
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    class Meta:
        app_label = 'news'
        db_table = 'event update'

    def __str__(self):
        return self.title

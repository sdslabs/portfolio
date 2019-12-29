from django.db import models

# Create your models here.


class Timeline(models.Model):
    """Model representing details of timeline"""
    timing = models.CharField(max_length=50)
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=500)

    class Meta:
        app_label = 'timeline'
        db_table = 'timeline'

    def __str__(self):
        return self.title

from django.db import models

# Create your models here.

class Project(models.Model):
    """"Models representing details of Project."""
    permalink = models.CharField(max_length=40, unique=True)
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=500)
    url = models.URLField(max_length=200)
    image = models.ImageField(upload_to='projects')
    color = models.CharField(max_length=15, blank=True)
    is_visible = models.BooleanField(default=False)

    class Meta:
        app_label = 'projects'
        db_table = 'project'

    def __unicode__(self):
        return '{0}: {1}'.format(self.title, self.url)

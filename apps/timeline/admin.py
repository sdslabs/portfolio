from django.contrib import admin

from .models import Timeline

# Register your models here.

@admin.register(Timeline)
class TimelineAdmin(admin.ModelAdmin):
    list_display = ('title', 'timing', 'description')
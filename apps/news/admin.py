from django.contrib import admin

from .models import Event, EventUpdate

# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('type', 'title', 'timing', 'description', 'description1', 'url', 'image', 'status')

@admin.register(EventUpdate)
class EventUpdateAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'description1', 'description2', 'url', 'image', 'event')

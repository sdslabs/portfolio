from rest_framework import serializers

from .models import Event, EventUpdate


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('types', 'priority', 'title', 'timing', 'shortDescription', 'fullDescription', 'url', 'image', 'is_visible' )


class EventUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventUpdate
        fields = ('title', 'timing', 'description', 'contactInfo', 'footNote', 'greetings', 'image', 'event')

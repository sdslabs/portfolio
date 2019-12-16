from rest_framework import serializers

from .models import Event, EventUpdate


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('type', 'title', 'timing', 'description', 'description1', 'url', 'image', 'status')


class EventUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventUpdate
        fields = ('title', 'description', 'description1', 'description2', 'image', 'event')

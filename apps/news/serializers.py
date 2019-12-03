from rest_framework import serializers

from .models import Event, AppUpdate, OnlineCompetition, EventUpdate


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('title', 'timing', 'description', 'description1', 'url', 'image', 'status')


class AppUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppUpdate
        fields = ('title', 'description', 'url')


class OnlineCompetitionSerializer(serializers.ModelSerializer):

    class Meta:
        model = OnlineCompetition
        fields = ('title', 'timing', 'description', 'url')


class EventUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventUpdate
        fields = ('title', 'description', 'description1', 'description2', 'image', 'event')

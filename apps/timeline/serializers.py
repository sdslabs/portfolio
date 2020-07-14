from rest_framework import serializers

from .models import Timeline


class TimelineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Timeline
        fields = ( 'timing', 'title', 'description' )
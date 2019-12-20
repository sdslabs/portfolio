from rest_framework import permissions, status
from rest_framework.decorators import (
    api_view,
    permission_classes,
    throttle_classes,
)
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle

from .models import Event, EventUpdate
from .serializers import EventSerializer, EventUpdateSerializer


@throttle_classes([
    AnonRateThrottle,
])
@api_view(['GET'])
@permission_classes((permissions.AllowAny, ))
def get_events(request):
    """
    Get a list of events
    """
    event = Event.objects.filter()
    serializer = EventSerializer(
        event, many=True, context={'request': request})
    response_data = serializer.data
    return Response(response_data, status=status.HTTP_200_OK)

@throttle_classes([
    AnonRateThrottle,
])
@api_view(['GET'])
@permission_classes((permissions.AllowAny, ))
def get_event_updates(request):
    """
    Get a list of updates
    """
    event_update = EventUpdate.objects.filter()
    serializer = EventUpdateSerializer(
        event_update, many=True, context={'request': request})
    response_data = serializer.data
    return Response(response_data, status=status.HTTP_200_OK)

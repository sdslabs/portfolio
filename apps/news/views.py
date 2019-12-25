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
    event_requested = request.query_params.get('title')
    if event_requested is not None:
        event = Event.objects.filter(title=event_requested)
        event_update = EventUpdate.objects.filter(event=event[0])
        event_serializer = EventSerializer(event, many=True, context={'request': request})
        event_update_serializer = EventUpdateSerializer(event_update, many=True, context={'request': request})
        response_data = {'event': event_serializer.data, 'event_update': event_update_serializer.data}
        return Response(response_data, status=status.HTTP_200_OK)
    else:
        event_array = []
        events = Event.objects.filter()
        for event in events:
            event_update = EventUpdate.objects.filter(event=event)
            event_serializer = EventSerializer(
                event, many=False, context={'request': request})
            event_update_serializer = EventUpdateSerializer(
                event_update, many=True, context={'request': request}
            )
            response_data = {'event': event_serializer.data, 'event_update': event_update_serializer.data}
            event_array.append(response_data)
        return Response(event_array, status=status.HTTP_200_OK)


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

from rest_framework import permissions, status
from rest_framework.decorators import (
    api_view,
    permission_classes,
    throttle_classes,
)
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle

# Create your views here.
from .models import Timeline
from .serializers import TimelineSerializer


@throttle_classes([
    AnonRateThrottle,
])
@api_view(['GET'])
@permission_classes((permissions.AllowAny, ))
def get_timeline(request):
    """
    Get a list of timeline
    """
    timeline = Timeline.objects.filter()
    serializer = TimelineSerializer(
        timeline, many=True, context={'request': request})
    response_data = serializer.data
    return Response(response_data, status=status.HTTP_200_OK)

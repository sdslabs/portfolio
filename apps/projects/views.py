from rest_framework import permissions, status
from rest_framework.decorators import (
    api_view,
    permission_classes,
    throttle_classes,
)
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle

from .models import Project
from .serializers import ProjectSerializer


@throttle_classes([
    AnonRateThrottle,
])
@api_view(['GET'])
@permission_classes((permissions.AllowAny, ))
def get_projects(request):
    """
    Get a list of projects
    """
    projects = Project.objects.filter(is_visible=True).order_by('title')
    serializer = ProjectSerializer(
        projects, many=True, context={'request': request})
    response_data = serializer.data
    return Response(response_data, status=status.HTTP_200_OK)

from rest_framework import viewsets

from .models import Profile
from .serializers import ReadOnlyUserSerializer


class ReadOnlyProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ReadOnlyUserSerializer

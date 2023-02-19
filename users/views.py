from rest_framework import viewsets

from .serializers import Profile, ReadOnlyUserSerializer
from .serializers import Project, ProjectSerializer


class ReadOnlyProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ReadOnlyUserSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

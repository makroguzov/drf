from rest_framework import serializers

from .models import Profile
from .models import Project


class ReadOnlyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('email', 'first_name', 'last_name')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('name', 'repo', 'contributors')

    @property
    def kwargs(self):
        return self.context.get('request').parser_context['kwargs']

    def create(self, validated_data):
        # Забирать владельца будем из запроса.
        # На будущее это нужно делать из данных аутентификации.
        return super().create({**validated_data,
                               'owner': Profile.objects.get(pk=self.kwargs['user_pk'])})

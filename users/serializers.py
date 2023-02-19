from rest_framework import serializers

from .models import Profile


class ReadOnlyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('email', 'first_name', 'last_name')

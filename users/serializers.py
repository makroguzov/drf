from rest_framework import serializers

from .models import Profile
from .models import Project
from .models import TODO


class ReadOnlyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'email', 'first_name', 'last_name')


class KwargsMixin:
    @property
    def kwargs(self):
        return self.context.get('request').parser_context['kwargs']


class ProjectSerializer(serializers.ModelSerializer, KwargsMixin):
    class Meta:
        model = Project
        fields = ('id', 'name', 'repo', 'contributors')

    def create(self, validated_data):
        # Забирать владельца будем из запроса.
        # На будущее это нужно делать из данных аутентификации.
        try:
            return super().create({**validated_data,
                                   'owner': Profile.objects.get(pk=self.kwargs['user_pk'])})
        except Profile.DoesNotExist as err:
            raise serializers.ValidationError(err)


class TODOSerializer(serializers.ModelSerializer, KwargsMixin):
    class Meta:
        model = TODO
        fields = '__all__'
        read_only_fields = ('creator', 'project', 'status', 'created_at', 'updated_at')

    def create(self, validated_data):
        try:
            return super().create({**validated_data,
                                   'creator': Profile.objects.get(pk=self.kwargs['user_pk']),
                                   'project': Project.objects.get(pk=self.kwargs['project_pk'])})
        # Это конечно может не самый разумный способ обработки ошибок.
        #   1) Хочется больше информативности
        #   2) Здесь не лучшее место, что бы это проверять.
        # В будущем перенесу все эти проверки на этап всяких штук с аутентификацией.
        # Надо будет еще проверять что пользователь является владельцем проекта и все такое.
        except (Profile.DoesNotExist,
                Project.DoesNotExist) as err:
            raise serializers.ValidationError(err)

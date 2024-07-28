from rest_framework import serializers

from users.serializers import CustomUserSerializer, ModeratorsSerializer
from .models import SocialNetworkModel, SocialTaskModel, UserTaskModel, TaskModeratorModel, TaskModel, TaskTypeModel


class TaskTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskTypeModel
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    related_user = CustomUserSerializer()

    class Meta:
        model = TaskModel
        fields = '__all__'


class TaskModeratorSerializer(serializers.ModelSerializer):
    related_user = CustomUserSerializer()
    related_moderator = ModeratorsSerializer()
    related_task = TaskSerializer()

    class Meta:
        model = TaskModeratorModel
        fields = '__all__'


class SocialNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialNetworkModel
        fields = '__all__'


class SocialTaskSerializer(serializers.ModelSerializer):
    related_task = TaskSerializer()
    related_social_network = SocialNetworkSerializer()

    class Meta:
        model = SocialTaskModel
        fields = '__all__'


class UserTaskSerializer(serializers.ModelSerializer):
    related_user = CustomUserSerializer()
    related_social_task = SocialTaskSerializer()

    class Meta:
        model = UserTaskModel
        fields = '__all__'

from rest_framework import viewsets

from tasks.models import TaskTypeModel, TaskModel, TaskModeratorModel, SocialNetworkModel, SocialTaskModel, \
    UserTaskModel
from tasks.serializers import UserTaskSerializer, SocialTaskSerializer, SocialNetworkSerializer, \
    TaskModeratorSerializer, TaskSerializer, TaskTypeSerializer


# Create your views here.

class TaskTypeViewSet(viewsets.ModelViewSet):
    queryset = TaskTypeModel.objects.all()
    serializer_class = TaskTypeSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer


class TaskModeratorViewSet(viewsets.ModelViewSet):
    queryset = TaskModeratorModel.objects.all()
    serializer_class = TaskModeratorSerializer


class SocialNetworkViewSet(viewsets.ModelViewSet):
    queryset = SocialNetworkModel.objects.all()
    serializer_class = SocialNetworkSerializer


class SocialTaskViewSet(viewsets.ModelViewSet):
    queryset = SocialTaskModel.objects.all()
    serializer_class = SocialTaskSerializer


class UserTaskViewSet(viewsets.ModelViewSet):
    queryset = UserTaskModel.objects.all()
    serializer_class = UserTaskSerializer

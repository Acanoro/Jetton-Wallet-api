from rest_framework import viewsets

from tasks.serializers import *


# Create your views here.

class TaskTypeViewSet(viewsets.ModelViewSet):
    queryset = TaskTypeModel.objects.all()
    serializer_class = TaskTypeSerializer
    http_method_names = ['get']


class TaskViewSet(viewsets.ModelViewSet):
    queryset = TaskModel.objects.filter(status=True)
    serializer_class = TaskSerializer
    http_method_names = ['get']


class TaskModeratorViewSet(viewsets.ModelViewSet):
    queryset = TaskModeratorModel.objects.all()
    serializer_class = TaskModeratorSerializer
    http_method_names = ['get', 'post', 'patch', 'put']


class SocialNetworkViewSet(viewsets.ModelViewSet):
    queryset = SocialNetworkModel.objects.all()
    serializer_class = SocialNetworkSerializer
    http_method_names = ['get']


class SocialTaskViewSet(viewsets.ModelViewSet):
    queryset = SocialTaskModel.objects.all()
    serializer_class = SocialTaskSerializer
    http_method_names = ['get', 'post', 'patch', 'put']


class UserTaskViewSet(viewsets.ModelViewSet):
    queryset = UserTaskModel.objects.all()
    serializer_class = UserTaskSerializer
    http_method_names = ['get']

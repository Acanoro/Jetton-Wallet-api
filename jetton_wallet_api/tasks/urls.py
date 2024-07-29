from django.urls import include, path
from rest_framework.routers import DefaultRouter

from tasks.views import *

router = DefaultRouter()
router.register(r'task-type', TaskTypeViewSet)
router.register(r'task', TaskViewSet)
router.register(r'task-moderator', TaskModeratorViewSet)
router.register(r'social-network', SocialNetworkViewSet)
router.register(r'social-task', SocialTaskViewSet)
router.register(r'user-task', UserTaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

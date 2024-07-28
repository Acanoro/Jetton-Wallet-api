from django.urls import include, path
from rest_framework.routers import DefaultRouter

from tasks.views import TaskTypeViewSet, TaskViewSet, TaskModeratorViewSet, SocialNetworkViewSet, SocialTaskViewSet, \
    UserTaskViewSet

router = DefaultRouter()
router.register(r'api/v1/task-type', TaskTypeViewSet)
router.register(r'api/v1/task', TaskViewSet)
router.register(r'api/v1/task-moderator', TaskModeratorViewSet)
router.register(r'api/v1/social-network', SocialNetworkViewSet)
router.register(r'api/v1/social-task', SocialTaskViewSet)
router.register(r'api/v1/user-task', UserTaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

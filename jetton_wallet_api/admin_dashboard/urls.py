from django.urls import include, path
from rest_framework.routers import DefaultRouter

from admin_dashboard.views import AdminDashboardViewSet

router = DefaultRouter()
router.register(r'api/v1/admin-dashboard', AdminDashboardViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

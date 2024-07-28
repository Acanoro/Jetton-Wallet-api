from rest_framework import serializers

from admin_dashboard.models import AdminDashboardModel


class AdminDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminDashboardModel
        fields = '__all__'

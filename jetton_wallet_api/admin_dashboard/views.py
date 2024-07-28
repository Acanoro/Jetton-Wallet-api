from django.shortcuts import render
from rest_framework import viewsets

from admin_dashboard.models import AdminDashboardModel
from admin_dashboard.serializers import AdminDashboardSerializer


# Create your views here.
class AdminDashboardViewSet(viewsets.ModelViewSet):
    queryset = AdminDashboardModel.objects.all()
    serializer_class = AdminDashboardSerializer

from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response

from users.serializers import *


# Create your views here.
class AvatarsViewSet(viewsets.ModelViewSet):
    queryset = AvatarsModel.objects.filter(active=True)
    serializer_class = AvatarsSerializer
    http_method_names = ['get']


class LanguagesViewSet(viewsets.ModelViewSet):
    queryset = LanguagesModel.objects.filter(active=True)
    serializer_class = LanguagesSerializer
    http_method_names = ['get']


class LeaderBoardViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by('balance')
    serializer_class = LeaderBoardSerializer
    http_method_names = ['get']


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class ModeratorsViewSet(viewsets.ModelViewSet):
    queryset = ModeratorsModel.objects.all()
    serializer_class = ModeratorsSerializer
    http_method_names = ['get']


class NameWalletViewSet(viewsets.ModelViewSet):
    queryset = NameWalletModel.objects.all()
    serializer_class = NameWalletSerializer
    http_method_names = ['get']


class TonWalletViewSet(viewsets.ModelViewSet):
    serializer_class = TonWalletSerializer

    def get_queryset(self):
        user = self.request.user
        custom_user = get_object_or_404(CustomUser, id=user.id)

        return TonWalletModel.objects.filter(related_user=custom_user)
    #
    # def list(self, request, *args, **kwargs):
    #     raise PermissionDenied("You are not allowed to access all records.")


class ReferralsViewSet(viewsets.ModelViewSet):
    serializer_class = ReferralsSerializer

    def get_queryset(self):
        queryset = ReferralsModel.objects.all()
        user_id = self.request.query_params.get('user_id', None)
        if user_id is not None:
            queryset = queryset.filter(related_user_id=user_id)
        return queryset


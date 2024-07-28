from rest_framework import viewsets

from users.models import AvatarsModel, LanguagesModel, CustomUser, ModeratorsModel, NameWalletModel, TonWalletModel, \
    ReferralsModel
from users.serializers import ReferralsSerializer, TonWalletSerializer, NameWalletSerializer, ModeratorsSerializer, \
    CustomUserSerializer, LanguagesSerializer, AvatarsSerializer


# Create your views here.
class AvatarsViewSet(viewsets.ModelViewSet):
    queryset = AvatarsModel.objects.all()
    serializer_class = AvatarsSerializer


class LanguagesViewSet(viewsets.ModelViewSet):
    queryset = LanguagesModel.objects.filter(active=True)
    serializer_class = LanguagesSerializer
    http_method_names = ['get', 'put', 'patch']


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class ModeratorsViewSet(viewsets.ModelViewSet):
    queryset = ModeratorsModel.objects.all()
    serializer_class = ModeratorsSerializer


class NameWalletViewSet(viewsets.ModelViewSet):
    queryset = NameWalletModel.objects.all()
    serializer_class = NameWalletSerializer


class TonWalletViewSet(viewsets.ModelViewSet):
    queryset = TonWalletModel.objects.all()
    serializer_class = TonWalletSerializer


class ReferralsViewSet(viewsets.ModelViewSet):
    queryset = ReferralsModel.objects.all()
    serializer_class = ReferralsSerializer

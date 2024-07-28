from rest_framework import serializers

from users.models import AvatarsModel, LanguagesModel, CustomUser, ModeratorsModel, NameWalletModel, TonWalletModel, \
    ReferralsModel


class AvatarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvatarsModel
        fields = '__all__'


class LanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguagesModel
        fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class ModeratorsSerializer(serializers.ModelSerializer):
    related_user = CustomUserSerializer()

    class Meta:
        model = ModeratorsModel
        fields = "__all__"


class NameWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = NameWalletModel
        fields = '__all__'


class TonWalletSerializer(serializers.ModelSerializer):
    related_name_wallet = NameWalletSerializer()
    related_user = CustomUserSerializer()

    class Meta:
        model = TonWalletModel
        fields = '__all__'


class ReferralsSerializer(serializers.ModelSerializer):
    related_user = CustomUserSerializer()
    related_user_referral = CustomUserSerializer()

    class Meta:
        model = ReferralsModel
        fields = '__all__'

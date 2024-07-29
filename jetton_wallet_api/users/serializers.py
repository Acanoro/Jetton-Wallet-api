from rest_framework import serializers

from users.models import *


class AvatarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvatarsModel
        fields = ['name', 'image']


class LanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguagesModel
        fields = ['name', 'iso_code']


class LeaderBoardSerializer(serializers.ModelSerializer):
    referrals_count = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ['username', 'balance', 'referrals_count']

    def get_referrals_count(self, obj) -> int:
        return ReferralsModel.objects.filter(related_user=obj).count()


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = super(CustomUserSerializer, self).create(validated_data)
        user.set_password(user.password)
        user.is_active = True
        user.save()

        return user


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

    class Meta:
        model = TonWalletModel
        fields = ['related_name_wallet', 'date', 'address']


class ReferralsSerializer(serializers.ModelSerializer):
    related_user_referral = CustomUserSerializer()

    class Meta:
        model = ReferralsModel
        fields = ['related_user_referral']

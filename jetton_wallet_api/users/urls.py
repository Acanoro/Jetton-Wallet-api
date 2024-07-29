from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views import *

router = DefaultRouter()
router.register(r'avatars', AvatarsViewSet)
router.register(r'languages', LanguagesViewSet)
router.register(r'leader-board', LeaderBoardViewSet)
router.register(r'users', CustomUserViewSet, basename='users')
router.register(r'moderators', ModeratorsViewSet)
router.register(r'name-wallets', NameWalletViewSet)
router.register(r'ton-wallets', TonWalletViewSet, basename='ton_wallet')
router.register(r'referrals', ReferralsViewSet, basename='referral')

urlpatterns = [
    path('', include(router.urls)),
]

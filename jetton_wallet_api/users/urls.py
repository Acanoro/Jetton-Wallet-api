from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views import AvatarsViewSet, LanguagesViewSet, CustomUserViewSet, ModeratorsViewSet, NameWalletViewSet, \
    ReferralsViewSet, TonWalletViewSet

router = DefaultRouter()
router.register(r'api/v1/avatars', AvatarsViewSet)
router.register(r'api/v1/languages', LanguagesViewSet)
router.register(r'api/v1/users', CustomUserViewSet)
router.register(r'api/v1/moderators', ModeratorsViewSet)
router.register(r'api/v1/name-wallets', NameWalletViewSet)
router.register(r'api/v1/ton-wallets', TonWalletViewSet)
router.register(r'api/v1/referrals', ReferralsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

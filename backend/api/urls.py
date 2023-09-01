from django.urls import include, path

from rest_framework.routers import DefaultRouter

from api.users.users_views import (
    AccountViewSet, OTPTokenCreateView, SendOTPCodeView)

app_name = 'api'

api_router_v1 = DefaultRouter()

api_router_v1.register(
    r'users',
    AccountViewSet,
    basename='users'
    )


urlpatterns = [
    path('', include(api_router_v1.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/send-otp/', SendOTPCodeView.as_view(), name='send_otp'),
    path('auth/token/login/', OTPTokenCreateView.as_view(), name='token_create'),
]

import random

from django.contrib.auth import get_user_model
from django.core.mail import send_mail

from django_otp.plugins.otp_totp.models import TOTPDevice

from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from djoser.views import UserViewSet
from djoser.views import TokenCreateView

from drf_spectacular.utils import extend_schema_view

from api.users.users_serializers import SendOTPCodeSerializer

from api.schemas import (create_schema, destroy_schema, list_schema,
                         partial_update_schema, retrieve_schema, update_schema)

from backend.settings import DEFAULT_FROM_EMAIL


User = get_user_model()


@extend_schema_view(
    list=list_schema, create=create_schema,
    retrieve=retrieve_schema, update=update_schema,
    partial_update=partial_update_schema, destroy=destroy_schema,
)
class AccountViewSet(UserViewSet):
    queryset = User.objects.all()
    search_fields = ('^username', '^email', '^first_name', '^last_name')


class OTPTokenCreateView(TokenCreateView):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.user
        device = TOTPDevice.objects.get(user=user)
        otp_code = request.data.get('otp_code')

        if not device.verify_token(otp_code):
            raise serializers.ValidationError('Invalid OTP code')

        token, _ = device.generate_challenge()

        response_data = {
            'auth_token': token.token,
            'expires_in': token.token_expires
        }

        return Response(response_data, status=status.HTTP_201_CREATED)


class SendOTPCodeView(APIView):
    serializer_class = SendOTPCodeSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        device = serializer.validated_data['device']

        otp_code = ''.join(random.choices('0123456789', k=6))

        device.token = otp_code
        device.save()

        send_mail(
            'OTP Code',
            f'Your OTP code is: {otp_code}',
            DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False
        )

        return Response(
            {'message': 'OTP code sent'},
            status=status.HTTP_200_OK
        )

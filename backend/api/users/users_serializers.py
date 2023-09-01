from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.contrib.auth import authenticate, get_user_model

from django_otp.plugins.otp_totp.models import TOTPDevice

from djoser.serializers import (UserCreateSerializer, UserSerializer,
                                TokenCreateSerializer)

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from backend.settings import (MAX_LENGTH_PASSWORD, MIN_LENGTH_PASSWORD,
                              MAX_LENGTH_USERNAME, MAX_LENGTH_EMAIL)

from users.validators import (validate_username, validate_password,
                              validate_first_name, validate_last_name)

User = get_user_model()


class CustomUserCreateSerializer(UserCreateSerializer):
    password = serializers.CharField(
        max_length=MAX_LENGTH_PASSWORD,
        required=True,
        write_only=True,
        validators=[
            MinLengthValidator(
                limit_value=MIN_LENGTH_PASSWORD,
                message='Password must be longer than 6 characters'
            ),
            MaxLengthValidator(
                limit_value=MAX_LENGTH_PASSWORD,
                message='Password must be shorter than 30 characters'
            ),
            validate_password
        ],
        help_text=(
            'Enter password.'
            'It must include lowercase and uppercase letters '
            'of the Latin alphabet and numbers.'
        ),
    )
    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                message='This email is already taken',
                queryset=User.objects.all()
            ),
            MaxLengthValidator(
                limit_value=MAX_LENGTH_EMAIL,
                message=(
                    'Email must be shorter than'
                    f'{MAX_LENGTH_EMAIL} characters'
                )
            )
        ],
        required=True
    )
    username = serializers.CharField(
        validators=[
            UniqueValidator(
                message='This username is already taken',
                queryset=User.objects.all()
            ),
            validate_username
        ],
        required=True
    )
    first_name = serializers.CharField(
        max_length=MAX_LENGTH_USERNAME,
        help_text='Enter your first name',
        validators=[validate_first_name],
        required=True
    )
    last_name = serializers.CharField(
        max_length=MAX_LENGTH_USERNAME,
        help_text='Enter your last name',
        validators=[validate_last_name],
        required=True
    )

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = (
            'id', 'email', 'first_name',
            'last_name', 'username', 'password'
        )


class CustomUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = User
        fields = (
            'id', 'email', 'first_name',
            'last_name', 'username'
        )


class CustomTokenCreateSerializer(TokenCreateSerializer):
    otp_code = serializers.CharField(write_only=True)
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user

    def validate(self, attrs):
        attrs = super().validate(attrs)

        otp_code = attrs.get('otp_code')
        user = attrs.get('user')

        device = TOTPDevice.objects.get(user=user)

        if not device.verify_token(otp_code):
            raise serializers.ValidationError('Invalid OTP code')

        return attrs


class SendOTPCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(username=email, password=password)
        if user is None:
            raise serializers.ValidationError('Invalid email or password')

        try:
            device = TOTPDevice.objects.get(user=user)
        except device.DoesNotExist:
            raise serializers.ValidationError('No OTP device found for this user')

        attrs['user'] = user
        attrs['device'] = device
        return attrs

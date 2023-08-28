import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

REGEX_USER = re.compile(r'^[\w.@+-]+\Z')
REGEX_PASSWORD = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z0-9_]+')


def validate_username(value):
    """
    Метод проверки username на корректность.
    """
    if not REGEX_USER.match(value):
        raise ValidationError(
            _('%(value)s is invalid username!'),
            params={'value': value},
        )
    return value


def validate_password(value):
    if not REGEX_PASSWORD.match(value):
        raise ValidationError(
            _(
                '%(value)s is invalid password! '
                'Password must contain at least one lowercase letter, '
                'one uppercase letter and one digit.'),
            params={'value': value},
        )
    return value


def validate_first_name(value):
    if not value.isalpha():
        raise serializers.ValidationError(
            'First name should only contain alphabetic characters.'
            )
    return value


def validate_last_name(value):
    if not value.isalpha():
        raise serializers.ValidationError(
            'Last name should only contain alphabetic characters.'
            )
    return value

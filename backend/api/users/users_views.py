from djoser.views import UserViewSet

from drf_spectacular.utils import extend_schema_view, extend_schema

# from rest_framework import status

# from .users_serializers import CustomUserCreateSerializer, CustomUserSerializer

from users.models import User


@extend_schema_view(
    list=extend_schema(
        summary="Get list of users",
        responses={
            200: {"description": "Successful operation"},
            401: {"description": "Unauthorized"},
            403: {"description": "Forbidden"},
        },
    ),
    create=extend_schema(
        summary="Create a new user",
        responses={
            201: {"description": "User created successfully"},
            400: {"description": "Bad request"},
        },
    ),
    retrieve=extend_schema(
        summary="Get user details",
        responses={
            200: {"description": "Successful operation"},
            401: {"description": "Unauthorized"},
            403: {"description": "Forbidden"},
            404: {"description": "User not found"},
        },
    ),
    update=extend_schema(
        summary="Update user details",
        responses={
            200: {"description": "User updated successfully"},
            400: {"description": "Bad request"},
            401: {"description": "Unauthorized"},
            403: {"description": "Forbidden"},
            404: {"description": "User not found"},
        },
    ),
    partial_update=extend_schema(
        summary="Partially update user details",
        responses={
            200: {"description": "User updated successfully"},
            400: {"description": "Bad request"},
            401: {"description": "Unauthorized"},
            403: {"description": "Forbidden"},
            404: {"description": "User not found"},
        },
    ),
    destroy=extend_schema(
        summary="Delete user",
        responses={
            204: {"description": "User deleted successfully"},
            401: {"description": "Unauthorized"},
            403: {"description": "Forbidden"},
            404: {"description": "User not found"},
        },
    ),
)
class AccountViewSet(UserViewSet):
    queryset = User.objects.all()
    search_fields = ('^username', '^email', '^first_name', '^last_name')

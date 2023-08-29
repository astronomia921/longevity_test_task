from djoser.views import UserViewSet

from drf_spectacular.utils import extend_schema_view

from api.schemas import (
    list_schema,
    create_schema,
    retrieve_schema,
    update_schema,
    partial_update_schema,
    destroy_schema,
)

from users.models import User


@extend_schema_view(
    list=list_schema,
    create=create_schema,
    retrieve=retrieve_schema,
    update=update_schema,
    partial_update=partial_update_schema,
    destroy=destroy_schema,
)
class AccountViewSet(UserViewSet):
    queryset = User.objects.all()
    search_fields = ('^username', '^email', '^first_name', '^last_name')

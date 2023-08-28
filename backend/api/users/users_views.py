from djoser.views import UserViewSet
from users.models import User


class AccountViewSet(UserViewSet):
    queryset = User.objects.all()
    search_fields = ('^username', '^email', '^first_name', '^last_name')

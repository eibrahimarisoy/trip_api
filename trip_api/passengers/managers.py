from django.contrib.auth.models import UserManager


class CustomUserManager(UserManager):
    def get(self, *args, **kwargs):
        return super().select_related('passenger',).get(*args, **kwargs)
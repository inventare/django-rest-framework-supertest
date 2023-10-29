from typing import Optional

from django.contrib.auth.models import AbstractUser

from .base import AuthenticationBase


class SessionAuthentication(AuthenticationBase):
    authentication_failed_exceptions = []

    def authenticate(self, user: Optional[AbstractUser]):
        if not user:
            return
        self.client.force_login(user)

__all__ = ['SessionAuthentication']

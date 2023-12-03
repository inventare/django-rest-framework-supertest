from typing import Optional

from django.contrib.auth.models import AbstractUser

from .base import AuthenticationBase


class SessionAuthentication(AuthenticationBase):
    """Implements adapter to use session with `AuthenticationBase` test utils."""

    def authenticate(self, user: Optional[AbstractUser]) -> None:
        """
        Authenticate an user with session.

        The method uses `APIClient.force_login()` method.

        Args:
            user: The user to authenticate.
        """
        if not user:
            return
        self.client.force_login(user)

__all__ = ['SessionAuthentication']

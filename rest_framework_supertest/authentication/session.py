from typing import Optional

from django.contrib.auth.models import AbstractUser
from django.http import HttpResponse

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

    def is_valid_auth_response(
        self,
        response: HttpResponse,  # noqa: ARG002
        user: AbstractUser,  # noqa: ARG002
    ) -> bool:
        """
        Check if a response is a valid authentication response for a user.

        Is not supported for session authentication.

        Args:
            response: The `HttpResponse` to check.
            user: The user to check if the reponse is valid for this user.
        """
        msg = (
            "is_valid_auth_response() method is not supported by session authentication"
        )
        raise NotImplementedError(msg)

__all__ = ['SessionAuthentication']

from typing import ClassVar, List, Optional

from django.contrib.auth.models import AbstractUser
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import APIException

from rest_framework_supertest.authentication import AuthenticationBase


class SimpleJWTAuthentication(AuthenticationBase):
    """
    Implements adapter to use SimpleJWT with `AuthenticationBase` test utils.

    Determinates `authenticate` function for the SimpleJWT and exceptions
    for authentication failed and unauthentication.
    """

    access_token_field = "access"  # noqa: S105
    refresh_token_field = "refresh"  # noqa: S105

    authentication_failed_exceptions: ClassVar[List[APIException]] = []
    unauthentication_exceptions: ClassVar[List[APIException]] = []

    def __init__(self, test_case):
        super().__init__(test_case)

        try:
            from rest_framework.exceptions import (
                AuthenticationFailed as BaseAuthenticationFailed,
            )
            from rest_framework_simplejwt.exceptions import (
                AuthenticationFailed,
                InvalidToken,
            )
            from rest_framework_simplejwt.serializers import TokenObtainSerializer

            self.authentication_failed_exceptions = [
                BaseAuthenticationFailed(
                    TokenObtainSerializer.default_error_messages["no_active_account"],
                    "no_active_account",
                )
            ]
            self.unauthentication_exceptions = [
                AuthenticationFailed(
                    _("Authorization header must contain two space-delimited values"),
                    code="bad_authorization_header",
                ),
                InvalidToken(
                    {
                        "detail": _("Given token not valid for any token type"),
                        "messages": [
                            {
                                "token_class": "AccessToken",
                                "token_type": "access",
                                "message": "Token is invalid or expired",
                            },
                        ],
                    }
                ),
                InvalidToken(
                    _("Token contained no recognizable user identification"),
                ),
                AuthenticationFailed(
                    _("User not found"),
                    code="user_not_found",
                ),
                AuthenticationFailed(
                    _("User is inactive"),
                    code="user_inactive",
                ),
                AuthenticationFailed(
                    _("The user's password has been changed."),
                    code="password_changed",
                ),
            ]
        except ImportError:
            msg = (
                "To use SimpleJWtAuthentication class, the"
                "rest_framework_simplejwt package should be installed."
            )
            raise ImportError(msg)

    def authenticate(self, user: Optional[AbstractUser]) -> None:
        """
        Authenticate an user with SimpleJWT token.

        Generates an AccessToken for the user and set HTTP_AUTHORIZATION
        header for the TestCase client.

        Args:
            user: The user to authenticate. If the user is None, the
              HTTP_AUTHORIZATION header is set to None.
        """
        if not user:
            self.client.credentials(HTTP_AUTHORIZATION=None)
            return

        from rest_framework_simplejwt.tokens import AccessToken

        token = str(AccessToken.for_user(user))
        self.client.credentials(HTTP_AUTHORIZATION="Bearer %s" % token)

    def is_valid_auth_response(
        self,
        response: HttpResponse,
        user: AbstractUser,
    ) -> bool:
        """
        Check if a response is a valid authentication response for a user.

        Args:
            response: The `HttpResponse` to check.
            user: The user to check if the reponse is valid for this user.
        """
        data = response.json()
        refresh_token = data.get(self.refresh_token_field)
        access_token = data.get(self.access_token_field)

        from rest_framework_simplejwt.exceptions import TokenError
        from rest_framework_simplejwt.settings import api_settings
        from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

        try:
            refresh_token = RefreshToken(refresh_token)
            refresh_token.verify()
        except TokenError:
            return False
        try:
            access_token = AccessToken(access_token)
            access_token.verify()
        except TokenError:
            return False

        refresh_user_id = refresh_token[api_settings.USER_ID_CLAIM]
        access_user_id = access_token[api_settings.USER_ID_CLAIM]

        return refresh_user_id == user.id and access_user_id == user.id


__all__ = ["SimpleJWTAuthentication"]

from typing import ClassVar, List, Optional

from django.contrib.auth.models import AbstractUser
from django.http import HttpResponse
from rest_framework.exceptions import APIException
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

from rest_framework_supertest.authentication import AuthenticationBase

from .errors import (
    NO_ACTIVE_ACCOUNT,
    TOKEN_NO_RECOGNIZABLE_USER_ID,
    TOKEN_NOT_VALID_FOR_ANY_TOKEN_TYPE,
    TWO_AUTORIZATION_PARTS,
    USER_IS_INACTIVE,
    USER_NOT_FOUND,
    USER_PASSWORD_CHANGED,
)


class SimpleJWTAuthentication(AuthenticationBase):
    """
    Implements adapter to use SimpleJWT with `AuthenticationBase` test utils.

    Determinates `authenticate` function for the SimpleJWT and exceptions
    for authentication failed and unauthentication.
    """

    access_token_field = 'access'  # noqa: S105
    refresh_token_field = 'refresh'  # noqa: S105

    authentication_failed_exceptions: ClassVar[List[APIException]] = [
        NO_ACTIVE_ACCOUNT,
    ]
    unauthentication_exceptions: ClassVar[List[APIException]] = [
        TWO_AUTORIZATION_PARTS,
        TOKEN_NOT_VALID_FOR_ANY_TOKEN_TYPE,
        TOKEN_NO_RECOGNIZABLE_USER_ID,
        USER_NOT_FOUND,
        USER_IS_INACTIVE,
        USER_PASSWORD_CHANGED,
    ]

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

        token = str(AccessToken.for_user(user))
        self.client.credentials(HTTP_AUTHORIZATION='Bearer %s' % token)

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


__all__ = ['SimpleJWTAuthentication']

from typing import ClassVar, List, Optional

from django.contrib.auth.models import AbstractUser
from rest_framework.exceptions import APIException
from rest_framework_simplejwt.tokens import AccessToken

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

__all__ = ['SimpleJWTAuthentication']

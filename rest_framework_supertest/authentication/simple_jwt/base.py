from typing import Optional

from django.db.models import Model
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
    authentication_failed_exceptions = [
        NO_ACTIVE_ACCOUNT,
    ]
    unauthentication_exceptions = [
        TWO_AUTORIZATION_PARTS,
        TOKEN_NOT_VALID_FOR_ANY_TOKEN_TYPE,
        TOKEN_NO_RECOGNIZABLE_USER_ID,
        USER_NOT_FOUND,
        USER_IS_INACTIVE,
        USER_PASSWORD_CHANGED,
    ]

    def authenticate(self, user: Optional[Model]):
        if not user:
            self.client.credentials(None)
            return

        token = str(AccessToken.for_user(user))
        self.client.credentials(HTTP_AUTHORIZATION='Bearer %s' % token)

__all__ = ['SimpleJWTAuthentication']

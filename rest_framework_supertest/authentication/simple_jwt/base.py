from typing import Optional
from django.db.models import Model
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt import exceptions as jwt_exceptions
from rest_framework_supertest.authentication import AuthenticationBase
from .errors import (
    NO_ACTIVE_ACCOUNT,
    TOKEN_NOT_VALID_FOR_ANY_TOKEN_TYPE,
    TWO_AUTORIZATION_PARTS,
)

class SimpleJWTAuthentication(AuthenticationBase):
    authentication_failed_exceptions = [
        NO_ACTIVE_ACCOUNT,
        TWO_AUTORIZATION_PARTS,
        TOKEN_NOT_VALID_FOR_ANY_TOKEN_TYPE,
    ]

    def authenticate(self, user: Optional[Model]):
        if not user:
            self.client.credentials(None)
            return
            
        token = str(AccessToken.for_user(user))
        self.client.credentials(HTTP_AUTHORIZATION='Bearer %s' % token)

__all__ = ['SimpleJWTAuthentication']

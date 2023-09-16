from typing import Optional
from django.db.models import Model
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework import exceptions
from .base import AuthenticationBase

class SimpleJWTAuthentication(AuthenticationBase):
    authentication_failed_exceptions = []

    def authenticate(self, user: Optional[Model]):
        if not user:
            self.client.credentials(None)
            return
            
        token = str(AccessToken.for_user(user))
        self.client.credentials('Bearer %s' % token)

__all__ = ['SimpleJWTAuthentication']

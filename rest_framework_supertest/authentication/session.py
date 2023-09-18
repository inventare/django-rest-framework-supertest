from typing import Optional
from django.db.models import Model
from rest_framework import exceptions
from .base import AuthenticationBase

class SessionAuthentication(AuthenticationBase):
    authentication_failed_exceptions = []

    def authenticate(self, user: Optional[Model]):
        self.client.force_login(user)

__all__ = ['SessionAuthentication']

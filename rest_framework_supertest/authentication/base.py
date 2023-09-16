from typing import Optional, List
from django.db.models import Model
from rest_framework.test import APIClient

class AuthenticationBase:
    client: APIClient
    authentication_failed_exceptions: List[Exception] = []

    def __init__(self, client: APIClient):
        self.client = client

    def authenticate(self, user: Optional[Model]):
        raise NotImplementedError("authenticate() method is not implemented")

__all__ = ['AuthenticationBase']

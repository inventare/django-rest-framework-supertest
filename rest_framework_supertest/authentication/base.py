from typing import Optional, List
from django.db.models import Model
from rest_framework import exceptions
from rest_framework.test import APIClient, APITestCase

class AuthenticationBase:
    client: APIClient
    test_case: APITestCase
    unauthentication_exceptions: List[Exception] = [exceptions.NotAuthenticated()]
    authentication_failed_exceptions: List[Exception] = []

    def __init__(self, test_case: APITestCase):
        self.test_case = test_case
        self.client = test_case.client

    def authenticate(self, user: Optional[Model]):
        raise NotImplementedError("authenticate() method is not implemented")

__all__ = ['AuthenticationBase']

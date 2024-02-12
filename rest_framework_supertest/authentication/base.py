from abc import ABC, abstractmethod
from typing import ClassVar, List, Optional

from django.contrib.auth.models import AbstractUser
from django.http import HttpResponse
from rest_framework import exceptions
from rest_framework.test import APIClient, APITestCase


class AuthenticationBase(ABC):
    """Base Class for Authentication Test Helper."""

    client: APIClient
    test_case: APITestCase
    unauthentication_exceptions: ClassVar[List[Exception]] = [
        exceptions.NotAuthenticated(),
    ]
    authentication_failed_exceptions: ClassVar[List[Exception]] = []

    def __init__(self, test_case: APITestCase):
        """
        Create an new instance of authentication util.

        Args:
            test_case: the currently APITestCase.
        """
        self.test_case = test_case
        self.client = test_case.client

    @abstractmethod
    def authenticate(self, user: Optional[AbstractUser]) -> None:
        """Authenticate an user for the requests."""

    @abstractmethod
    def is_valid_auth_response(
        self,
        response: HttpResponse,
        user: AbstractUser,
    ) -> bool:
        """Check if a auth response is valid for a user."""

__all__ = ['AuthenticationBase']

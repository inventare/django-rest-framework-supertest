from unittest.mock import MagicMock

from django.test import TestCase

from rest_framework_supertest.authentication import AuthenticationBase


class SimpleJWTTestCase(TestCase):
    def setUp(self) -> None:
        self.client = MagicMock()
        self.credentials = MagicMock()
        self.client.credentials = self.credentials
        self.test_case = MagicMock()
        self.test_case.client = self.client

    def test_error_instantiate(self) -> None:
        with self.assertRaises(TypeError):
            AuthenticationBase(self.test_case)

__all__ = []

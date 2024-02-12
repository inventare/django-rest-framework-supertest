from unittest.mock import MagicMock

from django.test import TestCase

from rest_framework_supertest.authentication import SessionAuthentication


class SimpleJWTTestCase(TestCase):
    def setUp(self) -> None:
        self.client = MagicMock()
        self.credentials = MagicMock()
        self.client.credentials = self.credentials
        self.test_case = MagicMock()
        self.test_case.client = self.client

        self.auth = SessionAuthentication(self.test_case)

    def test_error_is_valid_auth_response(self) -> None:
        with self.assertRaises(NotImplementedError):
            self.auth.is_valid_auth_response(MagicMock(), MagicMock())

__all__ = []

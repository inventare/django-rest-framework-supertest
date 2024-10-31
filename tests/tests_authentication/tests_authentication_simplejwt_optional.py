from unittest.mock import MagicMock, patch

from django.test import TestCase

from rest_framework_supertest.authentication import SimpleJWTAuthentication


class SimpleJWTOptionalTestCase(TestCase):
    def setUp(self) -> None:
        self.client = MagicMock()
        self.credentials = MagicMock()
        self.client.credentials = self.credentials
        self.test_case = MagicMock()
        self.test_case.client = self.client

    @patch("rest_framework_simplejwt.exceptions.AuthenticationFailed")
    def test_jwt_without_simplejwt(self, mock: MagicMock):
        mock.side_effect = ImportError()

        with self.assertRaises(ImportError):
            self.auth = SimpleJWTAuthentication(self.test_case)


__all__ = []

from unittest.mock import MagicMock

from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework_simplejwt.tokens import AccessToken

from rest_framework_supertest.authentication import SimpleJWTAuthentication


class SimpleJWTTestCase(TestCase):
    def setUp(self) -> None:
        self.client = MagicMock()
        self.credentials = MagicMock()
        self.client.credentials = self.credentials
        self.test_case = MagicMock()
        self.test_case.client = self.client

        self.auth = SimpleJWTAuthentication(self.test_case)
        self.password = "ANY PASSWORD"  # noqa: S105

    def get_user(self) -> User:
        return User.objects.create_user(
            username='any-user-here',
            email='example@example.com.br',
            password=self.password,
        )

    def test_jwt_authenticate_none_user(self) -> None:
        self.auth.authenticate(None)

        self.credentials.assert_called_once_with(HTTP_AUTHORIZATION=None)

    def test_jwt_authenticate_with_user(self) -> None:
        user = self.get_user()
        self.auth.authenticate(user)

        self.credentials.assert_called_once()
        kwargs = self.credentials.mock_calls[0].kwargs
        authorization = kwargs.get('HTTP_AUTHORIZATION')
        print(authorization)
        self.assertTrue(authorization.startswith('Bearer '))
        token = authorization.replace('Bearer ', '')
        token = AccessToken(token)

        self.assertEqual(token.payload.get('user_id'), user.pk)

__all__ = []

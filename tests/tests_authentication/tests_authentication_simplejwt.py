from unittest.mock import MagicMock

from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
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

    def get_user(
        self,
        email: str = 'example@example.com.br',
        username: str = 'any-user-here',
    ) -> User:
        return User.objects.create_user(
            username=username,
            email=email,
            password=self.password,
        )

    def test_jwt_authenticate_none_user(self) -> None:
        self.auth.authenticate(None)

        self.credentials.assert_called_once_with(HTTP_AUTHORIZATION=None)

    def test_jwt_authenticate_with_user(self) -> None:
        user = self.get_user()
        self.auth.authenticate(user)

        self.credentials.assert_called_once()

        _, kwargs = self.credentials.call_args
        authorization = kwargs.get('HTTP_AUTHORIZATION')
        self.assertTrue(authorization.startswith('Bearer '))
        token = authorization.replace('Bearer ', '')
        token = AccessToken(token)

        self.assertEqual(token.payload.get('user_id'), user.pk)

    def test_jwt_authentication_response(self) -> None:
        user = self.get_user()
        serializer = TokenObtainPairSerializer(data={
            'username': 'any-user-here',
            'password': self.password,
        })
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        response = MagicMock()
        response.status_code = 200
        response.headers = {}
        response.json = MagicMock(return_value=data)

        self.assertTrue(self.auth.is_valid_auth_response(response, user))

    def test_jwt_authentication_response_wrong_user(self) -> None:
        email = 'exxx@example.com.br'
        username = 'my_user'
        user2 = self.get_user()
        user = self.get_user(email=email, username=username)
        serializer = TokenObtainPairSerializer(data={
            'username': username,
            'password': self.password,
        })
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        response = MagicMock()
        response.status_code = 200
        response.headers = {}
        response.json = MagicMock(return_value=data)

        self.assertFalse(self.auth.is_valid_auth_response(response, user2))
        self.assertTrue(self.auth.is_valid_auth_response(response, user))

    def test_jwt_authentication_response_invalid_access(self) -> None:
        user = self.get_user()
        serializer = TokenObtainPairSerializer(data={
            'username': 'any-user-here',
            'password': self.password,
        })
        serializer.is_valid(raise_exception=True)
        data = {**serializer.validated_data, 'access': 'token'}
        response = MagicMock()
        response.status_code = 200
        response.headers = {}
        response.json = MagicMock(return_value=data)

        self.assertFalse(self.auth.is_valid_auth_response(response, user))

    def test_jwt_authentication_response_invalid_refresh(self) -> None:
        user = self.get_user()
        serializer = TokenObtainPairSerializer(data={
            'username': 'any-user-here',
            'password': self.password,
        })
        serializer.is_valid(raise_exception=True)
        data = {**serializer.validated_data, 'refresh': 'token'}
        response = MagicMock()
        response.status_code = 200
        response.headers = {}
        response.json = MagicMock(return_value=data)

        self.assertFalse(self.auth.is_valid_auth_response(response, user))

__all__ = []

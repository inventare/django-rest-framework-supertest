from django.test import TestCase
from rest_framework_simplejwt.settings import api_settings
from rest_framework_supertest.test import APITestCase
from rest_framework_supertest.models.helpers import setup_faker_fields
from rest_framework_supertest.models.base import create_faker
from rest_framework_supertest.authentication.simple_jwt import (
    TOKEN_NOT_VALID_FOR_ANY_TOKEN_TYPE,
    NO_ACTIVE_ACCOUNT,
    TWO_AUTORIZATION_PARTS,
    TOKEN_NO_RECOGNIZABLE_USER_ID,
    USER_NOT_FOUND,
    USER_IS_INACTIVE,
)
from rest_framework import exceptions
from django.http import Http404
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt import exceptions as jwt_exceptions
from rest_framework_supertest import shotcuts
from django.contrib.auth import get_user_model


User = get_user_model()

"""
class BaseLoggedAPITestCase:
    def setUp(self):
        setup_faker_fields(
            User,
            username=lambda faker: faker.word(),
            email=lambda faker: faker.email(),
            password=lambda faker: faker.word(),
        )
        return super().setUp()

    def test_with_authenticated_user(self):
        my_user = create_faker(User)
        self.authenticate(my_user)

        response = self.client.get('/api/logged/', {})
        self.assertResponseJson(response, {})

class JWTAPITestCase(BaseLoggedAPITestCase, APITestCase):
    authentication_class = 'rest_framework_supertest.authentication.SimpleJWTAuthentication'

class SessionAPITestCase(BaseLoggedAPITestCase, APITestCase):
    authentication_class = 'rest_framework_supertest.authentication.SessionAuthentication'


"""

class BookTestAPITestCase(APITestCase):
    authentication_class = 'rest_framework_supertest.authentication.SimpleJWTAuthentication'

    def setUp(self) -> None:
        setup_faker_fields(
            User,
            username=shotcuts.word,
            email=shotcuts.unique_email,
            password=shotcuts.word,
        )

        return super().setUp()

    def test_wrong_credentials(self):
        response = self.client.post('/api/token/', {
            'username': 'any',
            'password': 'any'
        })

        self.assertAPIException(response, NO_ACTIVE_ACCOUNT)
        self.assertAuthenticationFailed(response)

    def test_bearer_with_one_parts(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer')
        response = self.client.get('/api/logged/', {})

        self.assertAPIException(response, TWO_AUTORIZATION_PARTS)
        self.assertUnauthenticated(response)

    def test_bearer_with_three_parts(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer a 2')
        response = self.client.get('/api/logged/', {})

        self.assertAPIException(response, TWO_AUTORIZATION_PARTS)
        self.assertUnauthenticated(response)

    def test_bearer_with_invalid_token_type(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer a4456a5')
        response = self.client.get('/api/logged/', {})

        self.assertAPIException(response, TOKEN_NOT_VALID_FOR_ANY_TOKEN_TYPE)
        self.assertUnauthenticated(response)

    def test_with_authenticated_user(self):
        my_user = create_faker(User)
        self.authenticate(my_user)

        response = self.client.get('/api/logged/', {})
        self.assertResponseJson(response, {})

    def test_without_token_user_id(self):
        my_user = create_faker(User)
        from rest_framework_simplejwt.tokens import AccessToken
        token = AccessToken.for_user(my_user)
        del token[api_settings.USER_ID_CLAIM]

        self.client.credentials(HTTP_AUTHORIZATION='Bearer %s' % str(token))
        response = self.client.get('/api/logged/', {})

        self.assertAPIException(response, TOKEN_NO_RECOGNIZABLE_USER_ID)
        self.assertUnauthenticated(response)

    def test_with_token_invalid_user_id(self):
        my_user = create_faker(User)
        from rest_framework_simplejwt.tokens import AccessToken
        token = AccessToken.for_user(my_user)
        token[api_settings.USER_ID_CLAIM] = 0

        self.client.credentials(HTTP_AUTHORIZATION='Bearer %s' % str(token))
        response = self.client.get('/api/logged/', {})

        self.assertAPIException(response, USER_NOT_FOUND)
        self.assertUnauthenticated(response)

    def test_with_token_inactive_user_id(self):
        my_user = create_faker(User, { 'is_active': False })
        self.authenticate(my_user)
        response = self.client.get('/api/logged/', {})

        self.assertAPIException(response, USER_IS_INACTIVE)
        self.assertUnauthenticated(response)

    def test_validation(self):
        my_user = create_faker(User)
        self.authenticate(my_user)

        response = self.client.post('/api/logged/', {})
        self.assertHasValidationField(response, 'email', 'This field is required.')

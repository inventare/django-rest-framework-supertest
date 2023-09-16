from django.test import TestCase
from rest_framework_supertest.test import APITestCase
from rest_framework_supertest.models.helpers import setup_faker_fields
from rest_framework_supertest.models.base import create_faker
from rest_framework import exceptions
from django.http import Http404
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt import exceptions as jwt_exceptions
from django.contrib.auth import get_user_model


User = get_user_model()



class BookTestAPITestCase(APITestCase):
    wrong_credentials = exceptions.AuthenticationFailed(
        TokenObtainSerializer.default_error_messages["no_active_account"],
        "no_active_account",
    )
    two_parts_header_values = jwt_exceptions.AuthenticationFailed(
        _("Authorization header must contain two space-delimited values"),
        code="bad_authorization_header",
    )

    authentication_class = 'rest_framework_supertest.authentication.SimpleJWTAuthentication'

    def setUp(self):
        setup_faker_fields(
            User,
            username=lambda fake: fake.word(),
            email=lambda fake: fake.email(),
        )

        return super().setUp()

    def test_wrong_credentials(self):
        response = self.client.post('/api/token/', {
            'username': 'any',
            'password': 'any'
        })

        self.assertAPIException(response, self.wrong_credentials)

    def test_bearer_with_one_parts(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer')
        response = self.client.get('/api/logged/', {})

        self.assertAPIException(response, self.two_parts_header_values)

    def test_bearer_with_three_parts(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer a 2')
        response = self.client.get('/api/logged/', {})

        self.assertAPIException(response, self.two_parts_header_values)

    def test_with_authenticated_user(self):
        my_user = create_faker(User)
        self.authenticate(my_user)

        response = self.client.get('/api/logged/', {})
        self.assertEqual(response.status_code, 200)

# Create your tests here.

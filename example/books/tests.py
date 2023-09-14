from django.test import TestCase
from rest_framework_supertest.mixins import AssertAPIExceptionMixin
from rest_framework.test import APITestCase
from rest_framework import exceptions
from django.http import Http404
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt import exceptions as jwt_exceptions

class BookTestAPITestCase(AssertAPIExceptionMixin, APITestCase):
    wrong_credentials = exceptions.AuthenticationFailed(
        TokenObtainSerializer.default_error_messages["no_active_account"],
        "no_active_account",
    )
    two_parts_header_values = jwt_exceptions.AuthenticationFailed(
        _("Authorization header must contain two space-delimited values"),
        code="bad_authorization_header",
    )


    def test_wrong_credentials(self):
        response = self.client.post('/api/token/', {
            'username': 'any',
            'password': 'any'
        })

        self.assertAPIException(response, self.wrong_credentials)

    def test_bearer_with_one_parts(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer')
        response = self.client.post('/api/logged/', {})

        self.assertAPIException(response, self.two_parts_header_values)

    def test_bearer_with_three_parts(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer a 2')
        response = self.client.post('/api/logged/', {})

        self.assertAPIException(response, self.two_parts_header_values)
        

# Create your tests here.

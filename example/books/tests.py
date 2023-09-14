from django.test import TestCase
from rest_framework_supertest.mixins import AssertAPIExceptionMixin
from rest_framework.test import APITestCase
from rest_framework import exceptions
from django.http import Http404
from rest_framework_simplejwt.serializers import TokenObtainSerializer

class BookTestAPITestCase(AssertAPIExceptionMixin, APITestCase):
    exception = exceptions.AuthenticationFailed(
        TokenObtainSerializer.default_error_messages["no_active_account"],
        "no_active_account",
    )

    def test_aaaq(self):
        response = self.client.post('/api/token/', {
            'username': 'any',
            'password': 'any'
        })

        self.assertAPIException(response, self.exception)

# Create your tests here.

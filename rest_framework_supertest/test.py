from rest_framework.test import APITestCase as BaseAPITestCase
from rest_framework_supertest.mixins import (
    AssertAPIExceptionMixin,
    AssertAuthenticationMixin
)

class APITestCase(
    AssertAPIExceptionMixin,
    AssertAuthenticationMixin,
    BaseAPITestCase,
):
    pass

__all__ = ['APITestCase']

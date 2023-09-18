from rest_framework.test import APITestCase as BaseAPITestCase
from rest_framework_supertest.mixins import (
    AssertAPIResponseMixin,
    AssertAPIExceptionMixin,
    AssertAuthenticationMixin
)

class APITestCase(
    AssertAPIResponseMixin,
    AssertAPIExceptionMixin,
    AssertAuthenticationMixin,
    BaseAPITestCase,
):
    pass

__all__ = ['APITestCase']

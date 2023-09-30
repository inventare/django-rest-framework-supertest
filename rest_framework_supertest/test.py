from rest_framework.test import APITestCase as BaseAPITestCase
from rest_framework_supertest.mixins import (
    AssertAPIResponseMixin,
    AssertAPIExceptionMixin,
    AssertAuthenticationMixin,
    AssertAPIValidationMixin,
)

class APITestCase(
    AssertAPIResponseMixin,
    AssertAPIExceptionMixin,
    AssertAuthenticationMixin,
    AssertAPIValidationMixin,
    BaseAPITestCase,
):
    pass

__all__ = ['APITestCase']

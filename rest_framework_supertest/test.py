from rest_framework.test import APITestCase as BaseAPITestCase

from rest_framework_supertest.mixins import (
    AssertAPIExceptionMixin,
    AssertAPIResponseMixin,
    AssertAPIValidationMixin,
    AssertAuthenticationMixin,
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

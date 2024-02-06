from rest_framework.test import APITestCase as BaseAPITestCase

from rest_framework_supertest.mixins import (
    AssertAPIExceptionMixin,
    AssertAPIResponseMixin,
    AssertAPIValidationMixin,
    AssertAuthenticationMixin,
    AssertPaginationMixin,
    AssertSerializersMixin,
)


class APITestCase(
    AssertAPIResponseMixin,
    AssertAPIExceptionMixin,
    AssertAuthenticationMixin,
    AssertAPIValidationMixin,
    AssertSerializersMixin,
    AssertPaginationMixin,
    BaseAPITestCase,
):
    """
    Extended APITestCase for `rest_framework_supertest`.

    Comes with the `AssertAPIResponseMixin`, `AssertAPIExceptionMixin`,
    `AssertAuthenticationMixin` and `AssertAPIValidationMixin` mixins
    from the `rest_framework_supertest` package.
    """

__all__ = ['APITestCase']

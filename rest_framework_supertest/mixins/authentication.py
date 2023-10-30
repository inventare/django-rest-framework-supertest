from typing import Optional

from django.contrib.auth.models import AbstractUser
from django.http import HttpResponse
from django.utils.module_loading import import_string

from rest_framework_supertest.authentication import AuthenticationBase


class AssertAuthenticationMixin:
    """Implements a Mixin to use AuthenticationBase in APITestCase."""

    authentication_class = None
    _authentication: Optional[AuthenticationBase] = None

    @property
    def authentication(self) -> AuthenticationBase:
        """The authentication utils adapter instance."""
        if self._authentication:
            return self._authentication

        if not self.authentication_class:
            msg = (
                "To use authentication methods, "
                "authentication_class should be configured."
            )
            raise AttributeError(msg)

        if isinstance(self.authentication_class, str):
            try:
                authentication_class = import_string(self.authentication_class)
            except ImportError as exc:
                msg = "Could not import authentication_class '%(class)s'" % {
                    'class': self.authentication_class,
                }
                raise ImportError(msg) from exc
        else:
            authentication_class = self.authentication_class

        return authentication_class(self)

    def authenticate(self, user: AbstractUser) -> None:
        """
        Authenticate a user for the requests.

        Args:
            user: The user to authenticate.
        """
        return self.authentication.authenticate(user)

    def assert_unauthenticated(self, response: HttpResponse) -> None:
        """
        Assert if the response is an unauthenticated response.

        Args:
            response: The `HttpResponse` to check if is an unauthenticated
              response.
        """
        if not hasattr(self, 'assert_one_of_api_exceptions'):
            msg = (
                "To use assertUnauthenticated, assert_one_of_api_exceptions "
                "should be present. Add AssertAPIExceptionMixin to list "
                "of inherits mixins of your TestCase."
            )
            raise AttributeError(msg)

        if not self.authentication.unauthentication_exceptions:
            msg = (
                "None APIException provided into the unauthentication_exceptions "
                "field of the AuthenticationBase.",
            )
            raise AttributeError(msg)

        exceptions = self.authentication.unauthentication_exceptions
        self.assert_one_of_api_exceptions(response, exceptions)

    def assert_authentication_failed(self, response: HttpResponse) -> None:
        """
        Assert if the response is an authentication failed response.

        Args:
            response: The `HttpResponse` to check if is an authentication
              failed response.
        """
        if not hasattr(self, 'assert_one_of_api_exceptions'):
            msg = (
                "To use assertAuthenticationFailed, assert_one_of_api_exceptions "
                "should be present. Add AssertAPIExceptionMixin to list of inherits "
                "mixins of your TestCase."
            )
            raise AttributeError(msg)

        if not self.authentication.authentication_failed_exceptions:
            msg = (
                "None APIException provided into the authentication_failed_exceptions "
                "field of the AuthenticationBase.",
            )
            raise AttributeError(msg)

        exceptions = self.authentication.authentication_failed_exceptions
        self.assert_one_of_api_exceptions(response, exceptions)

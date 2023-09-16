from typing import List, Optional
import json
from django.http import HttpResponse
from django.db.models import Model
from django.utils.module_loading import import_string
from rest_framework_supertest.utils.exceptions import APIExceptionsUtils
from rest_framework_supertest.authentication import AuthenticationBase

class AssertAPIExceptionMixin:
    def assertAPIException(self, response: HttpResponse, exception):
        handler = APIExceptionsUtils(response, exception)
        data, status, headers = handler.exception_handler()

        self.assertEquals(response.status_code, status)
        self.assertEquals(json.dumps(data), json.dumps(response.json()))
        
        for header in headers.keys():
            value = headers.get(header)
            self.assertEquals(response.headers.get(header), value)

    def assertOneOfAPIExceptions(self, response: HttpResponse, exceptions: List[any]):
        found_one = False
        for exception in exceptions:
            handler = APIExceptionsUtils(response, exception)
            data, status, headers = handler.exception_handler()

            if response.status_code != status:
                continue
            if json.dumps(data) != json.dumps(response.json()):
                continue

            found_one = True
            for header in headers.keys():
                value = headers.get(header)

                if response.headers.get(header) != value:
                    found_one = False

            if found_one:
                break

        if not found_one:
            self.fail('None of the APIException\'s is raised to the response.')

class AssertAuthenticationMixin:
    authentication_class = None
    _authentication: Optional[AuthenticationBase] = None

    @property
    def authentication(self) -> AuthenticationBase:
        if self._authentication:
            return self._authentication
        
        if not self.authentication_class:
            msg = "To use authentication methods, authentication_class should be configured."
            raise AttributeError(msg)
        
        if type(self.authentication_class) == str:
            try:
                authentication_class = import_string(self.authentication_class)
            except ImportError:
                msg = "Could not import authentication_class '%s'" % self.authentication_class
                raise ImportError(msg)
        else:
            authentication_class = self.authentication_class

        return authentication_class(self.client)

    def authenticate(self, user: Model):
        return self.authentication.authenticate(user)
    
    def assertAuthenticationFailed(self, response):
        if not hasattr(self, 'assertOneOfAPIExceptions'):
            msg = (
                "To use assertAuthenticationFailed, assertOneOfAPIExceptions should be present. "
                "Add AssertAPIExceptionMixin to list of inherits mixins of your TestCase."
            )
            raise AttributeError(msg)
        
        if not self.authentication.authentication_failed_exceptions:
            msg = (
                "None APIException provided into the authentication_failed_exceptions field of "
                "the AuthenticationBase."
            )
            raise AttributeError(msg)
        
        exceptions = self.authentication.authentication_failed_exceptions
        self.assertOneOfAPIExceptions(response, exceptions)

__all__ = [
    'AssertAPIExceptionMixin',
    'AssertAuthenticationMixin',
]

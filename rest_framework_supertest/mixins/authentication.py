from typing import Optional
from django.db.models import Model
from django.utils.module_loading import import_string
from rest_framework_supertest.authentication import AuthenticationBase

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

        return authentication_class(self)

    def authenticate(self, user: Model):
        return self.authentication.authenticate(user)
    
    def assertUnauthenticated(self, response):
        if not hasattr(self, 'assertOneOfAPIExceptions'):
            raise AttributeError((
                "To use assertUnauthenticated, assertOneOfAPIExceptions should be present. "
                "Add AssertAPIExceptionMixin to list of inherits mixins of your TestCase."
            ))
        
        if not self.authentication.unauthentication_exceptions:
            raise AttributeError((
                "None APIException provided into the unauthentication_exceptions field of "
                "the AuthenticationBase."
            ))
        
        exceptions = self.authentication.unauthentication_exceptions
        self.assertOneOfAPIExceptions(response, exceptions)

    def assertAuthenticationFailed(self, response):
        if not hasattr(self, 'assertOneOfAPIExceptions'):
            raise AttributeError((
                "To use assertAuthenticationFailed, assertOneOfAPIExceptions should be present. "
                "Add AssertAPIExceptionMixin to list of inherits mixins of your TestCase."
            ))
        
        if not self.authentication.authentication_failed_exceptions:
            raise AttributeError((
                "None APIException provided into the authentication_failed_exceptions field of "
                "the AuthenticationBase."
            ))
        
        exceptions = self.authentication.authentication_failed_exceptions
        self.assertOneOfAPIExceptions(response, exceptions)

from typing import Optional, Union

from django.core.exceptions import PermissionDenied
from django.http import Http404, HttpResponse
from django.urls import resolve
from rest_framework import exceptions, status


class APIExceptionsUtils:
    """Utility class for work with `APIException`."""

    auth_exceptions = (
        exceptions.NotAuthenticated,
        exceptions.AuthenticationFailed,
    )

    def __init__(
        self,
        response: HttpResponse,
        exception: Union[Http404, PermissionDenied, exceptions.APIException],
    ):
        """
        Create a new instance of the `APIExceptionsUtils`.

        Args:
            response: The `HttpResponse` to use with utils.
            exception: The `APIException`, `Http404` or `PermissionDenied` exception
              to work with utils.
        """
        self.response = response
        self.request = getattr(response, 'wsgi_request', None)
        self.exc = exception
        self.transform_exception()

    def transform_exception(self) -> None:
        """
        Transform the exception.

        Verify if the exception is a Http404 or a PermissionDenied exception
        and transform it to equivalent APIException.
        """
        if isinstance(self.exc, Http404):
            self.exc = exceptions.NotFound(*(self.exc.args))
        if isinstance(self.exc, PermissionDenied):
            self.exc = exceptions.PermissionDenied(*(self.exc.args))

    def get_authenticate_header(self) -> Optional[str]:
        """
        Return the authentication header from the request.

        Try to check the path from the request and resolve the view
        function from it and instantiate the view and call the
        `get_authenticate_header()` from the view.

        Returns:
            None if the request is None. Otherwise, the result from the
            call of the `get_authenticate_header()` from the view instance.
        """
        if not self.request:
            return None

        path = self.request.path
        view_function, _, _ = resolve(path)
        view_class = view_function.view_class

        instance = view_class()
        return instance.get_authenticate_header(self.request)

    def handle_auth_headers(self) -> None:
        """
        Handle the authentication headers.

        If the exception is `NotAuthenticated` or `AuthenticationFailed`, gots the
        `WWW-Authenticate` header or coerce the response status_code to 403.
        """
        if isinstance(self.exc, self.auth_exceptions):
            # WWW-Authenticate header for 401 responses, else coerce to 403
            auth_header = self.get_authenticate_header()
            if auth_header:
                self.exc.auth_header = auth_header
            else:
                self.exc.status_code = status.HTTP_403_FORBIDDEN

    def get_headers(self) -> dict:
        """Return the response headers from the exception."""
        headers = {}

        if getattr(self.exc, 'auth_header', None):
            headers['WWW-Authenticate'] = self.exc.auth_header

        if getattr(self.exc, 'wait', None):
            headers['Retry-After'] = '%d' % self.exc.wait

        return headers

    def get_data(self) -> Union[list, dict]:
        """Return the response data from the exception."""
        if isinstance(self.exc.detail, (list, dict)):
            return self.exc.detail

        return {'detail': self.exc.detail}

    def exception_handler(self) -> (Union[list, dict], int, dict):
        """
        Handle the exception and return the informations to create the response.

        Returns:
            A tuple of three elements. The first element is the response data.
            The second element is the status_code and the last element is the
            response headers.
        """
        self.handle_auth_headers()

        if not isinstance(self.exc, exceptions.APIException):
            # TODO: work with uncaught exception here
            # https://github.com/encode/django-rest-framework/blob/master/rest_framework/views.py#L468
            msg = "TODO: Implements this before"
            raise NotImplementedError(msg)

        headers = self.get_headers()
        data = self.get_data()

        return data, self.exc.status_code, headers

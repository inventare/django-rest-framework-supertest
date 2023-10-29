from django.core.exceptions import PermissionDenied
from django.http import Http404, HttpResponse
from django.urls import resolve
from rest_framework import exceptions, status


class APIExceptionsUtils:
    auth_exceptions = (
        exceptions.NotAuthenticated,
        exceptions.AuthenticationFailed,
    )

    def __init__(self, response: HttpResponse, exception):
        self.response = response
        self.request = getattr(response, 'wsgi_request', None)
        self.exc = exception
        self.transform_exception()

    def transform_exception(self):
        if isinstance(self.exc, Http404):
            self.exc = exceptions.NotFound(*(self.exc.args))
        if isinstance(self.exc, PermissionDenied):
            self.exc = exceptions.PermissionDenied(*(self.exc.args))

    def get_authenticate_header(self):
        if not self.request:
            return None

        path = self.request.path
        view_function, _, _ = resolve(path)
        view_class = view_function.view_class

        instance = view_class()
        return instance.get_authenticate_header(self.request)

    def handle_auth_headers(self):
        if isinstance(self.exc, self.auth_exceptions):
            # WWW-Authenticate header for 401 responses, else coerce to 403
            auth_header = self.get_authenticate_header()
            if auth_header:
                self.exc.auth_header = auth_header
            else:
                self.exc.status_code = status.HTTP_403_FORBIDDEN

    def get_headers(self):
        headers = {}

        if getattr(self.exc, 'auth_header', None):
            headers['WWW-Authenticate'] = self.exc.auth_header

        if getattr(self.exc, 'wait', None):
            headers['Retry-After'] = '%d' % self.exc.wait

        return headers

    def get_data(self):
        if isinstance(self.exc.detail, (list, dict)):
            return self.exc.detail

        return {'detail': self.exc.detail}

    def exception_handler(self):
        self.handle_auth_headers()

        if not isinstance(self.exc, exceptions.APIException):
            ###
            ### TODO: https://github.com/encode/django-rest-framework/blob/master/rest_framework/views.py#L468
            ###
            raise NotImplementedError("TODO: Implements this before")

        headers = self.get_headers()
        data = self.get_data()

        return data, self.exc.status_code, headers

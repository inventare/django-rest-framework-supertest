import json
from django.http import Http404, HttpResponse
from rest_framework import exceptions
from django.core.exceptions import PermissionDenied

class AssertAPIExceptionMixin:
    def _transform_exception(self, exc):
        if isinstance(exc, Http404):
            return exceptions.NotFound(*(exc.args))
        if isinstance(exc, PermissionDenied):
            return exceptions.PermissionDenied(*(exc.args))
        return exc

    def _exception_handler(self, exc):
        exc = self._transform_exception(exc)
        
        if not isinstance(exc, exceptions.APIException):
            ###
            ### TODO: https://github.com/encode/django-rest-framework/blob/master/rest_framework/views.py#L468
            ###
            raise NotImplementedError("TODO: Implements this before")
            
        headers = {}
        ###
        ### TODO: https://github.com/encode/django-rest-framework/blob/master/rest_framework/views.py#L453
        ###
        if getattr(exc, 'auth_header', None):
            headers['WWW-Authenticate'] = exc.auth_header
        if getattr(exc, 'wait', None):
            headers['Retry-After'] = '%d' % exc.wait

        if isinstance(exc.detail, (list, dict)):
            data = exc.detail
        else:
            data = {'detail': exc.detail}

        return data, exc.status_code, headers

    def assertAPIException(self, response: HttpResponse, exception):
        data, status, headers = self._exception_handler(exception)

        self.assertEquals(response.status_code, status)
        self.assertEquals(json.dumps(data), json.dumps(response.json()))

        # TODO: assert headers
